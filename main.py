from data.file_manager import FileManager

if __name__ == "__main__":
    print("""
    reva-launcher v1.0
        Reva's Adventure super data generator

    Made by Chan <chanlugeon@protonmail.com> (chanlugeon.github.io)
""")
    manager = FileManager()
    while True:
        input("Press enter key if you want to generate super data.")
        manager.overwriteData()
        print("Generated super data.\nEnjoy Reva's Adventure!\n")