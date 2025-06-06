import os
import sys
import dotenv
import logging

class LogSectionData:
    '''Class to represent a section in the meslog file.
    Attributes:
        z (float): The z coordinate of the section.
        x (float): The x coordinate of the section.
        y (float): The y coordinate of the section.
        dia (float): The diameter of the section.
        ecc (float): The eccentricity of the section.
        ang (float): The angle of the section.
    '''
    def __init__(self, z, x,y,dia,ecc,ang):
        self.z = z
        self.x = x
        self.y = y
        self.dia = dia
        self.ecc = ecc
        self.ang = ang
    def __str__(self):
        return f"z: {self.z}, x: {self.x}, y: {self.y}, dia: {self.dia}, ecc: {self.ecc}, ang: {self.ang}"
    def __repr__(self):
        return f"z: {self.z}, x: {self.x}, y: {self.y}, dia: {self.dia}, ecc: {self.ecc}, ang: {self.ang}"  
    def __eq__(self, other):
        if isinstance(other, LogSectionData):
            return self.z == other.z and self.x == other.x and self.y == other.y and self.dia == other.dia and self.ecc == other.ecc and self.ang == other.ang
        return False    
    def __iter__(self):
        return iter(self.__dict__)
    def __next__(self):
        return next(iter(self.__dict__))
    def __copy__(self):
        return LogSectionData(self.z, self.x, self.y, self.dia, self.ecc, self.ang)
    def __str__(self):  
        return f"z: {self.z}, x: {self.x}, y: {self.y}, dia: {self.dia}, ecc: {self.ecc}, ang: {self.ang}"  
    def __repr__(self):
        return f"z: {self.z}, x: {self.x}, y: {self.y}, dia: {self.dia}, ecc: {self.ecc}, ang: {self.ang}"  
    
    
class TSawLog:
    '''
    Class to represent a saw log.
    Attributes:
        mill (str): The mill where the log was processed.
        species (str): The species of the log.
        quality (str): The quality of the log.
        log_id (str): The ID of the log.
        seg_num (int): The segment number of the log.
        num_sec (int): The number of sections in the log.
        wgt (float): The weight of the log.
        sections (list): A list of LogSectionData objects representing the sections of the log.
        log_file (str): The file path of the log.        
    '''
    def __init__(self, mill, species,quality, log_id, seg_num, num_sec, wgt, sections, log_file=None):
        self.mill = mill
        self.species = species
        self.quality = quality
        self.log_id = log_id
        self.seg_num = seg_num
        self.num_sec = num_sec
        self.wgt = wgt
        self.log_file = log_file
        self.sections = sections
        self.log_file = log_file
    def __init__(self, log_id, seg_num, num_sec, wgt, sections, log_file=None):
        self.log_id = log_id
        self.seg_num = seg_num
        self.num_sec = num_sec
        self.wgt = wgt
        self.log_file = log_file
        self.sections = sections
        self.log_file = log_file 
    def __str__(self):
        return f"mill: {self.mill}, species: {self.species}, quality: {self.quality}, log_id: {self.log_id}, seg_num: {self.seg_num}, num_sec: {self.num_sec}, wgt: {self.wgt}, sections: {self.sections}"
    def __repr__(self):
        return f"mill: {self.mill}, species: {self.species}, quality: {self.quality}, log_id: {self.log_id}, seg_num: {self.seg_num}, num_sec: {self.num_sec}, wgt: {self.wgt}, sections: {self.sections}"  
    def __eq__(self, other):
        if isinstance(other, TSawLog):
            return self.mill == other.mill and self.species == other.species and self.quality == other.quality and self.log_id == other.log_id and self.seg_num == other.seg_num and self.num_sec == other.num_sec and self.wgt == other.wgt and self.sections == other.sections
        return False    
    def __iter__(self):
        return iter(self.__dict__)
    def __next__(self):
        return next(iter(self.__dict__))
    def __copy__(self):
        return TSawLog(self.mill, self.species, self.quality, self.log_id, self.seg_num, self.num_sec, self.wgt, self.sections, self.log_file)   


