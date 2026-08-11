from dataclasses import dataclass,field
@dataclass
class Hub:
   hub_name:str          
   vehicles:list=field(default_factory=list)     