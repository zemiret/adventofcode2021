import binascii

class Literal:
    def __init__(self, version, packet_id, number):
        self.version = version
        self.packet_id = packet_id
        self.number = number

    def __str__(self):
        return f'v{self.version}, id: {self.packet_id}, val: {self.number}'


class Operator:
    def __init__(self, version, packet_id, subpackets):
        self.version = version
        self.packet_id = packet_id
        self.subpackets = subpackets

    def __str__(self):
        s = ""
        for packet in self.subpackets:
            s += '\t' + str(packet) + "\n"
        return f'{self.version}, id: {self.packet_id}: \n{s}'


def readfile(filename):
    with open(filename) as f:
        return bin(int(f.readline(), 16))[2:]


def advance_ptr(line, ptr, num):
    adv = ptr+num
    return line[ptr:adv], adv


def peek_type(line, ptr): # assumes ptr is packet start 
    t = bit_to_int(line[ptr+3:ptr+6])
    if t == 4:
        return 'lit'
    return 'op'


def decode_num(line, ptr):
    bits = ''
    group, ptr = advance_ptr(line, ptr, 5)
    while group[0] != '0':
        bits += group[1:]
        group, ptr = advance_ptr(line, ptr, 5)
    bits += group[1:]

    return bit_to_int(bits), ptr


def bit_to_int(bits):
    return int(bits, 2)


def decode_operator(line, ptr):
    version, ptr = advance_ptr(line, ptr, 3)
    packet_id, ptr = advance_ptr(line, ptr, 3)
    length_id, ptr = advance_ptr(line, ptr, 1)
    subpackets = []


    # TODO: HERE I STOPPED
    if length_id == '0':
        subpackets_bit_len, ptr = advance_ptr(line, ptr, 15)
        subpackets_bit_len = bit_to_int(subpackets_bit_len)

        total_bits_read = 0
        while total_bits_read < subpackets_bit_len:
            ptr_before = ptr

            if peek_type(line, ptr) == 'lit':
                packet, ptr = decode_literal(line, ptr)
            else:
                packet, ptr = decode_operator(line, ptr)

            subpackets.append(packet)
            total_bits_read += (ptr - ptr_before)

    else:
        subpackets_num, ptr = advance_ptr(line, ptr, 11)
        subpackets_num = bit_to_int(subpackets_num)
        for _ in range(subpackets_num):
            if peek_type(line, ptr) == 'lit':
                packet, ptr = decode_literal(line, ptr)
            else:
                packet, ptr = decode_operator(line, ptr)

            subpackets.append(packet)


    return Operator(bit_to_int(version), bit_to_int(packet_id), subpackets), ptr


def decode_literal(line, ptr):
    version, ptr = advance_ptr(line, ptr, 3)
    packet_id, ptr = advance_ptr(line, ptr, 3)
    num, ptr = decode_num(line, ptr)

    return Literal(bit_to_int(version), bit_to_int(packet_id), num), ptr


def sum_versions(op):
    v_sum = op.version
    for packet in op.subpackets:
        if packet.packet_id == 4: # lit
            v_sum += packet.version
        else:
            v_sum += sum_versions(packet)

    return v_sum


        
hexline = readfile('input1')
# hexline = readfile('testinput1')

#lit, ptr = decode_literal('110100101111111000101000', 0)
#print(lit)
#print(peek_type('110100101111111000101000', 0))


op, _ = decode_operator(hexline, 0)
print(sum_versions(op))

# op, ptr = decode_operator(hexline, 0)
# print(op)

