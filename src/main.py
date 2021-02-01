from src import file_reader as fr
from src import research
from src import directory_reader as dir_read

# The format of the data
# ID	Name	Hour(hour)	Machine	Seq
# 0	Petr Mazeev	16	IDSSA1	GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG

PATH_TO_RESULT = "result.txt"
LINE_DELIMITER = "\n"


def read_researches(dir_path):
    researches = []
    dir_reader = dir_read.DirReader(dir_path)
    for file_name in dir_reader:
        with fr.FileReader(file_name) as record_reader:
            for record in record_reader:
                researches.append(research.Research(record))
    return researches


def get_unique_machines(researches):
    return set(research.machine for research in researches)  # To record the names of all machines
    # or
    # unique_machines = set()
    # for research in researches:
    #     unique_machines.add(research.machine)
    # return unique_machines


def get_unique_scientist_name(researches):
    return set(research.full_name for research in researches)
    # unique_scientists = set()
    # for research in researches:
    #     unique_scientists.add(research.full_name)
    # return unique_scientists


def get_max_research_hour_for_machine(machines, researches):
    max_research_hour_for_machine = []  # To record the result
    for machine in machines:
        researches_per_hour = {}  # Creating a dictionary for counting
        for research in researches:
            if research.machine == machine:  # on this machine
                count_researches = researches_per_hour.get(research.hour, 0)  # We get how many have already counted this hour
                researches_per_hour[research.hour] = count_researches + 1  # Increase by 1
        max_researches_per_hour = max(researches_per_hour, key=lambda k: researches_per_hour[k])  # From the dictionary, we get the hour that is the busiest
        max_research_hour_for_machine.append([machine, max_researches_per_hour])
    return max_research_hour_for_machine


def write_result(file_name, max_research_hour_for_machine):
    with open(file_name, "w") as file_output:  # Open the file to display information about the machines
        for name, hours in max_research_hour_for_machine:
            file_output.write("Name:" + name + " Hours:" + hours + LINE_DELIMITER)


def write_researches_per_scientist(all_researchers, researches, dir_to_save="researcher_data"):
    for researcher in all_researchers:  # For all researchers, we create a file and write all the information about their
        # research into it
        with open(dir_to_save + "\\" + researcher + ".txt", "w") as file_output:
            for res in researches:
                if res.full_name == researcher:
                    file_output.write(res.machine + " " + res.hour + " " + res.seq + LINE_DELIMITER)


def main():
    dir_path = input()
    researches = read_researches(dir_path)
    unique_machines = get_unique_machines(researches)
    max_research_hour_for_machine = get_max_research_hour_for_machine(unique_machines, researches)
    unique_scientist_names = get_unique_scientist_name(researches)
    write_result(PATH_TO_RESULT, max_research_hour_for_machine)
    write_researches_per_scientist(unique_scientist_names, researches)


main()