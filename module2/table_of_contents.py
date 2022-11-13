chapter = int(input("Please enter the number of chapters \n"))
section = int(input("Please enter the number of sections \n"))
subsection = int(input("Please enter the number of subsections \n"))
for x in range(1, chapter+1):
    print(f"Chapter {x}")
    for y in range(1, section+1):
        print(f"-Section {x}.{y}")
        for z in range(1, subsection+1):
            print(f"--Subsection {x}.{y}.{z}")
