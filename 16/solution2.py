#!/usr/bin/python3

import math
import numpy as np
import re

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

data = "60556F980272DCE609BC01300042622C428BC200DC128C50FCC0159E9DB9AEA86003430BE5EFA8DB0AC401A4CA4E8A3400E6CFF7518F51A554100180956198529B6A700965634F96C0B99DCF4A13DF6D200DCE801A497FF5BE5FFD6B99DE2B11250034C00F5003900B1270024009D610031400E70020C0093002980652700298051310030C00F50028802B2200809C00F999EF39C79C8800849D398CE4027CCECBDA25A00D4040198D31920C8002170DA37C660009B26EFCA204FDF10E7A85E402304E0E60066A200F4638311C440198A11B635180233023A0094C6186630C44017E500345310FF0A65B0273982C929EEC0000264180390661FC403006E2EC1D86A600F43285504CC02A9D64931293779335983D300568035200042A29C55886200FC6A8B31CE647880323E0068E6E175E9B85D72525B743005646DA57C007CE6634C354CC698689BDBF1005F7231A0FE002F91067EF2E40167B17B503E666693FD9848803106252DFAD40E63D42020041648F24460400D8ECE007CBF26F92B0949B275C9402794338B329F88DC97D608028D9982BF802327D4A9FC10B803F33BD804E7B5DDAA4356014A646D1079E8467EF702A573FAF335EB74906CF5F2ACA00B43E8A460086002A3277BA74911C9531F613009A5CCE7D8248065000402B92D47F14B97C723B953C7B22392788A7CD62C1EC00D14CC23F1D94A3D100A1C200F42A8C51A00010A847176380002110EA31C713004A366006A0200C47483109C0010F8C10AE13C9CA9BDE59080325A0068A6B4CF333949EE635B495003273F76E000BCA47E2331A9DE5D698272F722200DDE801F098EDAC7131DB58E24F5C5D300627122456E58D4C01091C7A283E00ACD34CB20426500BA7F1EBDBBD209FAC75F579ACEB3E5D8FD2DD4E300565EBEDD32AD6008CCE3A492F98E15CC013C0086A5A12E7C46761DBB8CDDBD8BE656780"

#data = "D2FE28"
#data = "38006F45291200"
#data = "C200B40A82"
#data = "04005AC33890"
# https://stackoverflow.com/questions/1425493/convert-hex-to-binary

scale = 16 ## equals to hexadecimal
num_of_bits = 8


b = ""
for c in data:
    i_val = int(c, 16)
    b += f'{i_val:04b}'
print(f"{b}")


def parse_packet(cur_offset, b):
    print(f"checking {cur_offset} of {len(b)}")
    version = int(b[cur_offset:cur_offset+3],2)
    cur_offset += 3
    type_id = int(b[cur_offset:cur_offset+3],2)
    cur_offset += 3

    version_sum = version

    # type_id 4 means literal value. Each group prefixed with 1 except last group
    # other type_id =  operator
    if type_id == 4:
        first_bit = "1"
        full_value = ""
        while int(first_bit) == 1:
            (cur_offset, value, first_bit) = parse_value(cur_offset, b)
            print(f"first bit is {first_bit}")
            full_value += value
        print(f"literal value is {int(full_value,2)}")
        return (cur_offset, version_sum, int(full_value,2))
    else:
        ret_values = []
        length_type_id = int(b[cur_offset:cur_offset+1],2)
        cur_offset += 1
        #if 0, next 15 bits are a number of length in bits of sub packets for this
        if length_type_id == 0:
            subpacket_length = int(b[cur_offset:cur_offset+15],2)
            print(f"jumping {subpacket_length} {b[cur_offset:cur_offset+15]} offset {cur_offset}")
            cur_offset += 15

            end_offset = cur_offset + subpacket_length
            while cur_offset < end_offset:
                (cur_offset, version_sum_temp, full_value) = parse_packet(cur_offset, b)
                version_sum += version_sum_temp
                ret_values.append(int(full_value))
        #if 1 it's 11 bits representing the number of subpackets
        else:
            num_subpackets = int(b[cur_offset:cur_offset+11],2)
            cur_offset += 11

            for i in range(num_subpackets):
                (cur_offset, version_sum_temp, full_value) = parse_packet(cur_offset, b)
                version_sum += version_sum_temp
                ret_values.append(int(full_value))

        if type_id == 0:
            return (cur_offset, version_sum, sum(ret_values))
        if type_id == 1:
            prod = 1
            print(f"ret values is {ret_values}")
            for i in ret_values:
                prod *= i
            return (cur_offset, version_sum, prod)
        if type_id == 2:
            return (cur_offset, version_sum, min(ret_values))
        if type_id == 3:
            return (cur_offset, version_sum, max(ret_values))
        if type_id == 5:
            ret = 0
            if ret_values[0] > ret_values[1]:
                ret = 1
            return (cur_offset, version_sum, ret)
        if type_id == 6:
            ret = 0
            if ret_values[0] < ret_values[1]:
                ret = 1
            return (cur_offset, version_sum, ret)
        if type_id == 7:
            ret = 0
            if ret_values[0] == ret_values[1]:
                ret = 1
            return (cur_offset, version_sum, ret)

        print("OH SHIT")
    
def parse_value(cur_offset, b):
    first_bit = b[cur_offset:cur_offset+1]
    cur_offset += 1
    value = b[cur_offset:cur_offset+4]
    cur_offset += 4
    print(f"parsed literal {first_bit} {value} at offset {cur_offset}")
    return (cur_offset, value, first_bit)

cur_offset = 0
v_num_sum = 0

(cur_offset, version_sum_temp, final_value) = parse_packet(cur_offset, b)
v_num_sum += version_sum_temp

print(f"final value {final_value}")
        
