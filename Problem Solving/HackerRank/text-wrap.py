import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    # for wl in word_list:
    #     # print(wl)
    #     result = '\n'.wl
    result = '\n'.join(word_list)
    return result

if __name__ == '__main__':
    string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    max_width = 4
    result = wrap(string, max_width)
    print(result)
    # print('ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ')   # Need to make the single string like this
    # for r in result:
    #     print(r)