
class BSGraph:
  
#function to read input and to create edge and vertices
 def readActMovfile(self,inputfile): #1
   f=open(inputfile,"r")
   f=f.read().lower().split("\n")
   graph={}
   def addEdge(graph,vertices,u,v): 
	   graph[vertices]=u,v
   
     #   graph[vertices]=value
   def addEdge_1(graph,vertices,u): 
	   graph.setdefault(vertices,[]).append(u)


    # declaration of graph as dictionary 
   for i in range(0,len(f)):
     we=f[i].split("/")  
     if len(we)==3 :   
       addEdge(graph,we[0].strip(),we[1].strip(),we[2].strip())
       addEdge(graph,we[0].strip(),we[1].strip(),we[2].strip())
       addEdge_1(graph,we[1].strip(),we[0].strip())
       addEdge_1(graph,we[2].strip(),we[0].strip())
     else :
       addEdge_1(graph,we[0].strip(),we[1].strip())
       addEdge_1(graph,we[1].strip(),we[0].strip())
       
   return graph

#to display the edges and vertices 
 def displayActMov(self,graph,file,input_file): #2
    f=open(input_file,"r")
    f=f.read().lower().split("\n")
    act=[]
    mov=[]
    for i in range(0,len(f)):
     we=f[i].split("/")  
     if len(we)==3 :   
       mov.append(we[0])
       act.append(we[1])
       act.append(we[2])
     else :
       mov.append(we[0])
       act.append(we[1])
    print(mov)
    print(" ")
    print(set(act))
    
    file.write("--------Function displayActMov--------") 
    file.write("\n") 
   
#    print(movies)
    file.write("Total Number of movies: "+str(len(mov)))
    
    
#    actors = {k for k in list(graph.keys())[10:]}
#    print(actors)
    file.write("\n"+"Total Number of actors: "+str(len(act)))
    file.write("\n")
    
    file.write("\n"+"List of movies :")
    
    
    file.write("\n"+str(mov))
    
    file.write("\n")
    file.write("\n"+"List of actors :")
    
    file.write("\n"+str(act))
    file.write("\n")
    
    
    
    file.write("----------------------------------------- ")
    file.write("\n")

#to display the movies in which the actor acted
 def displayMoviesOfActor(self,graph,actor): #3 
     
    if actor not in graph.keys():
        return "We are not having the relevant movies of actor " + str(actor)
    else :
        return graph[actor]

#to display the actors acted in the movie
 def displayActorsOfMovie(self,graph,movie): #4
   if movie not in graph.keys():
        return "We are not having the relevant actor's of  movies " + str(movie)
   else : 
       return graph[movie]


# to find the relation between two movies
 def findMovieRelation(self, start, end,graph,path=[]):  #5
        path = path + [start]
        if start == end:
            return path
        if start not in  graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = BSGraph.findMovieRelation(self,node, end, graph, path)
                if newpath: return newpath
        return None


#to find trans relation between two movies 
 def   findMovieTransRelation(self,start, end,graph,path=[]): #6
        path = path + [start]
        if start == end:
            return path
        if start not in  graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = BSGraph.findMovieTransRelation(self,node, end, graph, path)
                if newpath: return newpath
        return None

#main_function
if __name__ == "__main__": 
    
    # to read the promptsPS2 file to give the dynamic input by user for testing
    prompt_input = open("promptsPS2.txt", "r") 
    prompt_input=prompt_input.read().lower()         # to read data promptsPS2 file
    split_prom=prompt_input.split("\n")
    
    # to write data into outputPS2 file   
    file = open("outputPS2.txt", "w") 
    
    #to declare the class
    graph = BSGraph()  
    
    # function to read input and to create vertices and edges using dictionary 
    graph_up=graph.readActMovfile("./inputPS2.txt")  #1 st function
    
    
    # function to display movies and actors and total number of movies and actors 
    graph.displayActMov(graph_up,file,"./inputPS2.txt") #2 nd function
    
        
    #two same functons to display movies of the actors with different inputs  #3 rd function

    file.write("\n")
    file.write("--------Function displayMoviesOfActor-------- ")
    file.write("\n")
    file.write("List of Movies: "+str(graph.displayMoviesOfActor(graph_up,split_prom[0][13:]))) # 3.a
    file.write("\n")
    file.write("List of Movies: "+str(graph.displayMoviesOfActor(graph_up,split_prom[1][13:])))#3.b
    file.write("\n")
    file.write("----------------------------------------- ")
    file.write("\n")
    
    
    
   #two samne function to display actors of movies with different inputs #4 th function

    file.write("\n")
    file.write("--------Function displayActorsOfMovie -------- ")
    file.write("\n")

    file.write("List of actors: "+str(graph.displayActorsOfMovie(graph_up,split_prom[2][13:])))#4a
    file.write("\n")

    file.write("List of actors: "+str(graph.displayActorsOfMovie(graph_up,split_prom[3][13:]))) #4c
    file.write("\n")
    file.write("----------------------------------------- ")
    file.write("\n")
    
   # to find relation between two movies  #5th function
    
    file.write("\n")
    file.write("--------Function findMovieRelation -------- ")
    file.write("\n")
    w=split_prom[4][9:]
    movie1=w.split(":")[0].strip()
    movie2=w.split(":")[1].strip()


    file.write("Movie A: "+str(movie1)+"\n"+"Movie B: "+str(movie2))  
    file.write("\n")

    a=graph.findMovieRelation(movie1,movie2,graph_up)#function directly writen to promtPS2 file
    if len(a)==3:
     file.write("Related Yes: "+str(a[1]))
     file.write("\n")
    else :
     file.write("Two movies has no relation ")
     file.write("\n")
    file.close
    
    
    file.write("\n")
    w=split_prom[5][9:]
    movie1=w.split(":")[0].strip()
    movie2=w.split(":")[1].strip()


    file.write("Movie A: "+str(movie1)+"\n"+"Movie B: "+str(movie2))
    file.write("\n")
    a=graph.findMovieRelation(movie1,movie2,graph_up)#function directly writen to promtPS2 file
    if len(a)==3:
     file.write("Related Yes: "+str(a[1]))
     file.write("\n")
    else :
     file.write("Two movies has no relation ")
     file.write("\n")
    
   # to trans relation  between two movies  #6

    file.write("\n")
    file.write("--------Function findMovieTransRelation --------  ")
    file.write("\n")
    w=split_prom[6][9:]
    movie1=w.split(":")[0].strip()
    movie2=w.split(":")[1].strip()

    file.write("Movie A: "+str(movie1)+"\n"+"Movie B: "+str(movie2))
    file.write("\n")

    if (graph.findMovieTransRelation(movie1,movie2,graph_up))==None: #function directly writen to promtPS2 file
      file.write("There is no TransRelation between two movies")
      file.write("\n")
    else:    
       file.write("Related : "+str(graph.findMovieTransRelation(movie1,movie2,graph_up)))#function directly writen to promtPS2 file
       file.write("\n")
    file.write("----------------------------------------- ")
    file.write("\n")




    w=split_prom[7][9:]
    movie1=w.split(":")[0].strip()
    movie2=w.split(":")[1].strip()

    file.write("Movie A: "+str(movie1)+"\n"+"Movie B: "+str(movie2))
    file.write("\n")


    if (graph.findMovieTransRelation(movie1,movie2,graph_up))==None:
       file.write("Not related , There is no TransRelation between two movies")
       file.write("\n")
    else:    
       file.write("Related : "+str(graph.findMovieTransRelation(movie1,movie2,graph_up)))
       file.write("\n")
    file.write("----------------------------------------- ")
    file.write("\n")
    file.close
#from matplotlib import pyplot
#import numpy as np
#import timeit
#from functools import partial
#import random
#
#def fconst(N):
#    """
#    O(1) function
#    """
#    x = 1
#
#def flinear(N):
#    """
#    O(n) function
#    """
#    x = [i for i in range(N)]
#
#def fsquare(N):
#    """
#    O(n^2) function
#    """
#    for i in range(N):
#        for j in range(N):
#            x = i*j
#
#def fshuffle(N):
#    # O(N)
#    random.shuffle(list(range(N)))
#
#def fsort(N):
#    x = list(range(N))
#    random.shuffle(x)
#    x.sort()
#
#def plotTC(fn, nMin, nMax, nInc, nTests):
#    """
#    Run timer and plot time complexity
#    """
#    x = []
#    y = []
#    for i in range(nMin, nMax, nInc):
#        N = i
#        testNTimer = timeit.Timer(partial(fn, N))
#        t = testNTimer.timeit(number=nTests)
#        x.append(i)
#        y.append(t)
#    p1 = pyplot.plot(x, y, 'o')
#    #pyplot.legend([p1,], [fn.__name__, ])
#
## main() function
#def main():
#    print('Analyzing Algorithms...')
#
#    plotTC(fconst, 10, 1000, 10, 10)
#    plotTC(flinear, 10, 1000, 10, 10)
#    plotTC(fsquare, 10, 1000, 10, 10)
#    #plotTC(fshuffle, 10, 1000, 1000, 10)
#    plotTC(fsort, 10, 1000, 10, 10)
#
#    # enable this in case you want to set y axis limits
#    #pyplot.ylim((-0.1, 0.5))
#    
#    # show plot
#    pyplot.show()
#
## call main
#if __name__ == '__main__':
#    main()
