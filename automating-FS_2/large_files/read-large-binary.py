with open("bbb63736373.jpg", "rb") as source_file:
    while True:
        chunk = source_file.read(1024)
        if chunk:
            process_data(chunk)
        else:
            break
            
