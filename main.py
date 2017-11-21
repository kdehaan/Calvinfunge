import field
#import interpreter
#import translator




def main():
    filename = input("Code location: ")
    if not filename:
        filename = "testfunge.cf"
    new_field = field.Field(filename)
    new_field.print_matrix()
    new_field.pointer_value()




if __name__ == '__main__':
    main()