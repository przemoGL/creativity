def extract_temperature_logs(file):
    """
    Function to extract only temperature data lines from file and save result to another file.
    :param file: path to txt type log [str]
    :return: extracted temperature logs [list]
    """

    temperature_logs = []

    with open(file, "r") as input_file:
        for line in input_file:
            if 'temperature' in line:
                temperature_logs.append([line.rstrip()])
        with open("result.txt", "w") as output:
            for record in temperature_logs:
                output.writelines(record)
            output.write('\nQuantity: ' + str(len(temperature_logs)))

    return temperature_logs
