class university:
    def __init__(self, country, city, program, TOEFL_IELTS=None, GRE=None, research_centres=None):
        self.country = country
        self.city = city
        self.program = program
        self.TOEFL_IELTS = TOEFL_IELTS
        self.GRE = GRE
        self.research_centres = research_centres
    
    def give_info(self):
        pass

    def to_dict(self):
        pass

class person:
    def __init__(self, name, last_name, university, main_topic_research, selected_research=None):
        self.name = name
        self.last_name = last_name
        self.university = university

    def give_info(self):
        pass

    def affinity(self):
        pass

    def show_research(self):
        pass

    def add_research(self):
        pass