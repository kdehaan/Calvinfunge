import executor


def main():
    filename = input("Code location: ")
    if not filename:
        filename = "testfunge.cf"

    executor.Executor(filename)


if __name__ == '__main__':
    main()