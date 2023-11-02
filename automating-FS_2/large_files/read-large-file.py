with open("big-data.txt", "r") as source_file:
    with open("big_data_corrected.txt", "w") as target_file:
        for line in source_file:
            target_file.write(line)
            
