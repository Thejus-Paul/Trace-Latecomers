import pickle 
write_file = open("./global/9D.obj", 'rb') 
object_pi2 = pickle.load(write_file)
print(object_pi2)