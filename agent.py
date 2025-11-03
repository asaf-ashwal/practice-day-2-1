
from abc import ABC, abstractmethod

class AgencyDirector:  
    isinstance = None
    def __init__(self,dir):
        self.dir = dir
    def __new__(cls, *arg):
        print('isinstance', isinstance)
        if cls.isinstance is None:
            cls.isinstance = super().__new__(cls)
            print('creat')
        return cls.isinstance
    def __str__(self):
        return  self.dir

    
class Agent():
    total_agents = 0
    def __init__(self, code_name:str, clearance_level: int, director:AgencyDirector):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agents += 1
        
        
    def gets_agent_name(self):
        return input('enter your name: ')
    
    def report(self):
        return f'Agent: {self.code_name} reporting. Clearance Level: {self._clearance_level}'
    
    def _clearance_level_increase(self):
        self._clearance_level += 1
    
    def _clearance_level_reduce(self):
        if self._clearance_level > 1:
            self._clearance_level -= 1
        else: print('agent at clearance level of 1 cennot lower it')
    @classmethod
    def total_agents_number(cls):
        print(f'you got totle of {cls.total_agents} agents.')
        
    
        
x = Agent('bird',5,AgencyDirector('asaf'))
x = Agent('bird',5,AgencyDirector('asaf'))
x = Agent('bird',5,AgencyDirector('asaf'))

x.report()


class Mission:
    def __init__(self, mission_name:str , target_location:str , assigned_agent:Agent ):
        self.assigned_agent = assigned_agent
        self.mission_name = mission_name
        self.target_location = target_location
        
    def report(self):
        print(f'Mission: {self.mission_name} Target: {self.target_location}, Agent: {self.assigned_agent.report()}')
        
# my_agent = Agent('bird',2)
# x = Mission('birds','usa',my_agent)
# my_agent._clearance_level_reduce()
# print(my_agent.report())


class FieldAgent(Agent):
    def __init__(self, code_name, clearance_level, region:str):
        super().__init__(code_name, clearance_level)
        self.region = region
    def report(self):
        return super().report() + '. region: ' + self.region
    
# my_agent = FieldAgent('bird',2, 'bla')
# print(my_agent.report())

class CyberAgent(Agent):
    def __init__(self, code_name, clearance_level, specialty):
        super().__init__( code_name, clearance_level,)
        self.specialty = specialty
    def report(self):
        return super().report() + '. specialty: ' + self.specialty
    
    
# agent1 = CyberAgent('flowar', 1, "hacking")
# agent2 = FieldAgent('summer', 2, 'blaa')
# l = [
#     agent1,
#     agent2
#     ]
# def agents_printer(agents:list):
#     for a in agents:
# print(agent1.report())
    
# agents_printer(l)
# Agent.total_agents_number()
    
    
    
