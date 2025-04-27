def reverse_scramble(scrambled):
    assert len(scrambled) == 64

    # Step 1: Undo x[1::2] + x[0::2]
    odds = scrambled[:32]
    evens = scrambled[32:]
    x = [''] * 64
    x[1::2] = odds
    x[0::2] = evens

    # Step 2: Undo the flag[-i::-8] slicing logic
    flag = [''] * 64
    for slice_index in range(8):  # corresponds to -8 to -1 offset
        for step in range(8):  # 8 characters per slice
            x_index = slice_index * 8 + step
            flag_index = step * 8 + (7 - slice_index)
            flag[flag_index] = x[x_index]

    return ''.join(flag)[::-1]      


scrambled_input = "Z2yFm7bCjR6SMWOCSiw{wqKWoJxTtxP4Hf74mQZ4qmghcu1mdX9HND7u8oxF}JsR"
original_flag = reverse_scramble(scrambled_input)
print(original_flag)
