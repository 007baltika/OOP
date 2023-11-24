# Реализуйте класс Config , который соответствует шаблону синглтон и
# описывает конфигурационный объект с фиксированными параметрами. 

# Присоздании экземпляра класс не должен принимать никаких аргументов.

# При первом вызове конструктора класса Config должен создаваться и
# возвращаться экземпляр этого класса, а при последующих вызовах должен
# возвращаться экземпляр, созданный при первом вызове.

class Config:
    
    _examples = []
    
    def __new__(cls):
        
        Config._examples.append(object.__new__(cls))
        
        if len(Config._examples) > 1:
            first_example = Config._examples[0]
            return first_example
        else:
            return object.__new__(cls) 
    
    def __init__(self):
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'
        

# TEST_1:
config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)
print()
# TEST_2:
config1 = Config()
config2 = Config()
config3 = Config()

print(config1 is config2)
print(config1 is config3)
print()
# TEST_3:
config1 = Config()
config2 = Config()

print(config1.program_name is config2.program_name)
print(config1.environment is config2.environment)
print(config1.loglevel is config2.loglevel)
print(config1.version is config2.version)
print()
# TEST_4:
config = Config()
configs = [Config() for _ in range(1000)]
print(all(item is config for item in configs))
print()
# TEST_5:
config = Config()
print('program_name' in config.__dict__)
print('environment' in config.__dict__)
print('loglevel' in config.__dict__)
print('version' in config.__dict__)        