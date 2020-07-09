import keyword
#------------------------------FUNCTIONS--------------------------------------------------------

#create parsing
def parsing_create_query(query_type,keywords,table_name,attr_name_list,datatype_name_list):
    print("\n")
    print("\n")
    print("************************CREATE QUERY PARSING************************")
    print("Query Type : ->",query_type)
    print("Keywords :->")
    print("---------------------> ",keywords[0])
    print("----------------------------> ",keywords[1])
    print("Table Name :->")
    print("---------------------> ",table_name)
    print("--------------------------> (")
    print("------------------------------------>  Attribute           Datatype")
    for i in range(len(attr_name_list)):
     print("------------------------------------------------>",attr_name_list[i],"                  ",datatype_name_list[i])

    print("_______________________________________________ )  ;")
        
#drop parsing
def parsing_drop_query(query_type,keywords,table_name):
    print("\n")
    print("\n")
    print("************************DROP QUERY PARSING************************")
    print("Query Type : ->",query_type)
    print("Keywords :->")
    print("---------------------> ",keywords[0])
    print("----------------------------> ",keywords[1])
    print("Table Name :->")
    print("---------------------> ",table_name)
    print("---------------------------> ; ")    

#select parsing
def parsing_select_query(query_type,attributes_list,keywords,table_name,condition_variables_list,operator):
    print("\n")
    print("\n")
    print("************************SELECT QUERY PARSING************************")
    print("Query Type : ->",query_type)
    print("Keywords :->")
    print("---------------------> ",keywords[0])
    print("Attributes Name :->")
    for i in range(len(attributes_list)):
        print("------------------------------------->",attributes_list[i])

    #with where or without where
    if len(keywords)==3: #with where
        print("Keywords :->")
        print("-------------------------------------------->",keywords[2])
        print("Table Name :->")
        print("---------------------------------------------->",table_name)
        print("Keywords :->")
        print("-------------------------------------------------->",keywords[1])
        print("Condition :->")
        print("------------------------------------------------------->attribute 1: ",condition_variables_list[0])
        print("------------------------------------------------------->operator : ",operator)
        print("------------------------------------------------------->attribute 2: ",condition_variables_list[1])
        
    elif len(keywords)==2:#without where
        print("Keywords :->")
        print("-------------------------------------------->",keywords[1])
        print("Table Name :->")
        print("---------------------------------------------->",table_name)

    print("-------------------------------------------------------------------------------> ; ")

#insert parsing
def parsing_insert_query(query_type,keywords,table_name,attr_list,val_list):
    print("\n")
    print("\n")
    print("************************INSERT QUERY PARSING************************")
    print("Query Type : ->",query_type)
    print("Keywords :->")
    print("---------------------> ",keywords[0])
    print("---------------------> ",keywords[1])
    print("Table Name :->")
    print("-------------------------> ",table_name)
    print("-----------------------------> ( ")
    print("Attributes Name ->      ","keyword --> ", keywords[2],"     Corresponding Values")
    for i in range(len(attr_list)):
        print(" ",attr_list[i],"    ------------------------------------------------------------------   ",val_list[i])
    print("---------------------------------------------------------   ) ;")

#parsing update
def parsing_update_query(query_type,keywords,table_name,attr_name_list,val_list,condition_variables_list,operator):
    print("\n")
    print("\n")
    print("************************UPDATE QUERY PARSING************************")
    print("Query Type : ->",query_type)
    print("Keywords :->")
    print("---------------------> ",keywords[0])
    print("Table Name :->")
    print("--------------------------->",table_name)
    print("Keywords :->")
    print("---------------------> ",keywords[1])
    print("Attribute Name ","=","       Value   ")
    for i in range(len(attr_name_list)):
        print(attr_name_list[i],"                          ",val_list[i])
    if len(keywords)==3:
        print("Keywords ->")
        print("--------------------------------------->",keywords[2])
        print("Condition :->")
        print("----------------------------------------------->attribute 1: ",condition_variables_list[0])
        print("----------------------------------------------->operator : ",operator)
        print("----------------------------------------------->attribute 2: ",condition_variables_list[1])

    print("-------------------------------------------------------------------------------> ; ")

#parsing delete
def parsing_delete_query(query_type,keywords,table_name,condition_variables_list,operator):
    print("\n")
    print("\n")
    print("************************DELETE QUERY PARSING************************")
    print("Query Type : ->",query_type)
    print("Keywords :->")
    print("---------------------> ",keywords[0])
    print("---------------------> ",keywords[1])
    print("Table Name :->")
    print("--------------------------->",table_name)
    if len(keywords)==3:
        print("Keywords ->")
        print("--------------------------------------->",keywords[2])
        print("Condition :->")
        print("----------------------------------------------->attribute 1: ",condition_variables_list[0])
        print("----------------------------------------------->operator : ",operator)
        print("----------------------------------------------->attribute 2: ",condition_variables_list[1])

    print("-------------------------------------------------------------------------------> ; ")



#extra \n removal
def remove_n(list):
    for i in range(len(list)):
      list[i]=list[i].strip()
    return list

#extra space removal
def remove_space(list):
     if '' in list:
          while '' in list:
               list.remove('')
     return list

#seprate , function
def seprate_(str):
    list=[]
    if ',' not in str:
        list.append(str)
        return list
    if ',' in str:
        list=list.split(',')
        temp_list=[]
        for i in range(len(list)-1):
            temp_list.append(list[i])
            temp_list.append(',')
        temp_list.append(list[-1])
        return temp_list

def check_datatype(str):
    datatype_list=["CHAR","VARCHAR","BINARY","VARBINARY","TINYBLOB","TINYTEXT","TEXT","BLOB","MEDIUMTEXT","MEDIUMBLOB","LONGTEXT","LONGBLOB","BOOL","BOOLEAN","INT","INTEGER","BIGINT","MEDIUMINT","FLOAT","DOUBLE","DATE","TIMESTAMP","TIME","YEAR"]
    if str not in datatype_list:
        return 0
    else:
        return 1

#variable validity check
def variable_validity_check(str):
    #print(str)
    str=str.strip()
    MyList=["WHERE","where","CREATE","create","DROP",'drop',"SELECT","select","INSERT","insert","UPDATE","update","DELETE","delete"]
    if str.isidentifier() and not(keyword.iskeyword(str) and str not in MyList):
        return 1
    else:
        return 0

#case checking
def case_check(str):
    if str.isupper() or str.islower():
        return 1
    else:
        return 0

#condition checking function
def condition_check(list):
    if (variable_validity_check(list[0]) or list[0].isdigit()) and (variable_validity_check(list[1]) or list[1].isdigit()) :
        return 1
    else:
        return 0
    
def value_validity_check(value):
    value=value.strip()
    if value.isdigit() :
        return 1
    else:
        return 0
    
#checking semicolon
def check_semicolon(list):
     if list[-1]==';':
          return 1
     else:
          return 0
     
#checking create statement
def check_create(list):
    query_type="CREATE QUERY"
    print("__________INSIDE CREATE FUNCTION_____________")    
    a=list[0]
    b=list[1]
    keywords=[a,b]
    attr_name_list=[]
    datatype_name_list=[]
    if (a=="create" and b=="table") or (a=="CREATE" and b=="TABLE"):
        new_list=list[2:]
        #print("New List : ",new_list)
        s="@" #delimeter
        s=s.join(new_list)
        if '(' in s and ')' in s:
            index1=s.index('(')
            index2=s.index(')')
            table_name=s[:index1-1]
            table_name=table_name.strip() #to remove whitespaces
            #print("Table Name : ",table_name)
            if variable_validity_check(table_name)==0:
                print("Error :-- Invalid Table Name")
                return 0
            else: #correct table name
                temp_str=s[index1+1:index2]
                temp_str=temp_str.strip() #to remove whitespaces
                #print("Temp_str : ",temp_str)
                temp_list=temp_str.split(',')
                #print("Temp_list",temp_list)
                count=len(temp_list) #number of colums
                check=1 # to check if any of the datatype or column name is incorrect
                for i in range(len(temp_list)):
                 #print("Inside loop : ",i)
                 check_list=temp_list[i].split('@') # to check data type and columns name
                 check_list=remove_space(check_list) #so that there will be no empty element
                 #print("Check List : ",check_list)
                 if len(check_list) !=2: 
                     print("Error :-- Invalid Attributes Initailzation")
                     return 0
                 else:
                    attr_name=check_list[0]
                    data_type=check_list[1]
                    attr_name_list.append(attr_name)
                    datatype_name_list.append(data_type)
                    #print("col : ",attr_name)
                    #print("data_type : ",data_type)
                    if variable_validity_check(attr_name)==1 and check_datatype(data_type)==1:
                        #print("Correct : ",check_list)
                        continue
                    else:
                        print("Error :-- Invalid Attribute Name or Datatype")
                        check=0
                        return 0
                if check==1:
                    print("Success : Create Query Pass")
                    parsing_create_query(query_type,keywords,table_name,attr_name_list,datatype_name_list)
        else:
            print("Error :-- Invalid Use of  (  or ) ")
            return 0
    else : #error
        return 0       

#checking drop statement
def check_drop(list):
    query_type="DROP QUERY"
    print("__________INSIDE DROP FUNCTION_____________")    
    a=list[0]
    b=list[1]
    table_name=list[2]
    if (a=="DROP" and b=="TABLE") or(a=="drop" and b=="table"):
        if variable_validity_check(table_name)==1:
            print("Drop Statement Pass")
            keywords=[a,b]
            parsing_drop_query(query_type,keywords,table_name)
            return 1
        else:
            print("Error :- Invalid Table Name ")
            return 0
    else:
        return 0
   
            
#checking select statement
def check_select(list):
     query_type="SELECT QUERY"
     print("__________INSIDE SELECT FUNCTION_____________")    
     a=list[0]
     attributes_list=[]
     keywords=[a] #select
     condition_variables_list=[]
     operator=""
     if a=="select" or a=="SELECT":
         if "where" in list or "WHERE" in list: #select with where condition
          #print("Inside where condition")
          if "where" in list:
           keywords.append("where")
           index=list.index("where")
          elif "WHERE" in list:
           keywords.append("WHERE")
           index=list.index("WHERE")

          list1=list[:index] #select without query list
          list1.append(";")
          list2=list[index:] #condition list
          #print(list1)
          #print(list2)
          
          #for list1 checking(equal to without where condition)
          table_name=list1[-2]
          #print("Table Name : ",table_name)
          if variable_validity_check(table_name)==1:
                 #print("Correct Table name")
                 b=list1[-3]
                 if b=="FROM" or b=="from":
                     if b=="FROM":
                         keywords.append("FROM")
                     if b=="from":
                         keywords.append("from")
                         
                     #print("inside from")
                     
                     #attributes name checking
                     col_names_list=list1[1:len(list1)-3] #after select before from
                     s=" "
                     #s.strip()
                     s=s.join(col_names_list)
                     #print("s=",s)
                     s.strip()
                     if  (s != "") and ( s=="*" or ( ',' not in s and variable_validity_check(s)==1)): #single attribute name
                         print("Creat Statement Pass(Without Condition)")
                         attributes_list.append(s)
                         #
                     elif ',' in s  :
                         #print("inside , condition")
                         check=1
                         #print(col_names_list)
                         #print(s)
                         temp_col_name_list=s.split(',')
                         #print(temp_col_name_list)
                         #print("hi")
                         for k in range(len(temp_col_name_list)):
                             #print("inside loop : ",k)
                             #print(temp_col_name_list[k])
                             x=temp_col_name_list[k]
                             if variable_validity_check(x)==1:
                                 #print("Inside col name check condition")
                                 attributes_list.append(x)
                                 continue
                             else:
                                 print("Error :-- Invalid Attribute Name -- ",temp_col_name_list[k])
                                 check=0
                                 return 0
                         print("Create Statement Pass(Without Condition)")
                     else:
                         print("Error :-- After Select Before From")
                         return 0
                 else: #incorrect from use
                     print("Error :-- FROM/from Missing")
                     return 0
          else:
              print("Error :-- Invalid Table Name")
              return 0            

          #print(list2)
            
          #for list2 checking( where condition)
          s=""
          size=len(list2)
          condition_list=list2[1:size-1] #excluding ;
          #print(condition_list)
          s=s.join(condition_list)
          #print(s)
          element_list=[]
          if "<=" in s:
              element_list=s.split("<=")
              operator="<="
          elif ">=" in s:
              element_list=s.split(">=")
              operator=">="
          elif "<>" in s:
              element_list=s.split("<>")
              operator="<>"
          elif '=' in s:
              element_list=s.split('=')
              operator="="
          elif '<' in s:
              element_list=s.split('<')
              operator="<"
          elif '>' in s:
              element_list=s.split('>')
              operator=">"
          elif '&' in s:
              element_list=s.split('&')
              operator="&"
          elif '|' in s:
              element_list=s.split('|')
              operator="|"
              
          condition_variables_list=element_list
          #print("Splitted list : ",element_list)
          if len(element_list) != 2:
              print("Error :-- Invalid Condition")
              return 0
          if condition_check(element_list)==1:
              print("Select Statement Pass(With Condition)")
              parsing_select_query(query_type,attributes_list,keywords,table_name,condition_variables_list,operator)
          else:
              print("Error :-- Invalid Condition")
              return 0
          

         else: #wihout where condition
             table_name=list[-2]
             #print("Table Name : ",table_name)
             if variable_validity_check(table_name)==1:
                 #print("Select Table name")
                 b=list[-3]
                 if b=="FROM" or b=="from":
                     #print("Inside from")
                     if b=="FROM":
                         keywords.append("FROM")
                     if b=="from":
                         keywords.append("from")
                 
                     #columns name checking
                     col_names_list=list[1:len(list)-3]
                     s=" "
                     s=s.join(col_names_list)
                     s.strip()
                     if (s != "") and ( s=="*" or ( ',' not in s and variable_validity_check(s)==1)):
                         attributes_list.append(s)
                         print("Select Statement Pass")
                         parsing_select_query(query_type,attributes_list,keywords,table_name,condition_variables_list,operator)
                         #ok
                     elif ',' in s:
                         check=1
                         #print(col_names_list)
                         #print(s)
                         temp_col_name_list=s.split(',')
                         #print(temp_col_name_list)
                         for k in range(len(temp_col_name_list)):
                             if variable_validity_check(temp_col_name_list[k])==1:
                                 attributes_list.append(temp_col_name_list[k])
                                 #print("Inside col name check condition")
                                 continue
                             else:
                                 print("Error :-- Invalid Attribute Name -- ",temp_col_name_list[k])
                                 check=0
                                 return 0
                         print("Select Statement Pass")
                         parsing_select_query(query_type,attributes_list,keywords,table_name,condition_variables_list,operator)
                     else:
                          return 0
                 else: #incorrect from use
                     print("Error :-- FROM/from Missing")
                     return 0
             else:
                 print("Error :-- Invalid Table Name")
                 return 0            
     else:
         #if not = to select or SELECT
         return 0


    
#checking insert statement
def check_insert(list):
 query_type="INSERT QUERY"
 print("__________INSIDE INSERT FUNCTION_____________")    
 a=list[0]
 b=list[1]
 keywords=[a,b]
 if (a=="insert" and b=="into") or (a=="INSERT" and b=="INTO"):
     #to do
     temp_list=list[2:]
     s=" "
     s=s.join(temp_list)
     count1=s.count('(')
     count2=s.count(')')
     if not(count1==2 and count2==2):
         print("Error :-- Invalid use of ( or )")
         return 0
     else:
         index=s.index('(')
         table_name=s[:index]
         #print("Table name : ",table_name)
         if variable_validity_check(table_name)==1:
             if "VALUES" in s or "values" in s:
                 if "values" in s:
                  temp_list=s.split("values")
                  keywords.append("values")
                 elif "VALUES" in s:
                     temp_list=s.split("VALUES")
                     keywords.append("VALUES")

                 #print("Splitted List : ",temp_list)

                 if len(temp_list)!=2:
                     print("Error :-- Invalid use of VALUES Keyword")
                     return 0
                 else:
                  str1=temp_list[0]
                  #print("Str1 : ",str1)
                  index1=str1.index('(')
                  index2=str1.index(')')
                  str1=str1[index1+1:index2] #list of attributes name
                  
                  str2=temp_list[1]
                  #print("Str2 :",str2)
                  index1=str2.index('(')
                  index2=str2.index(')')
                  str2=str2[index1+1:index2]
                  
                  #print("Str1 : ",str1)
                  #print("Str2 :",str2)
                  
                  attr_list=str1.split(',')
                  val_list=str2.split(',')
                  if len(attr_list) == len(val_list):
                      for k in range(len(attr_list)):
                          if (variable_validity_check(attr_list[k])==1):
                              #print("Correct name : ",attr_list[k])
                              continue
                          else:
                               print("Error :-- Invalid Attribute Name")
                               return 0
                      for k in range(len(val_list)):
                          #print(val_list[k])
                          s=val_list[k]
                          s.strip()
                          if (variable_validity_check(val_list[k])==1):
                              #print("Correct name : ",val_list[k])
                              continue
                          else:
                               continue
                               return 0

                      print("Insert Statement Pass") #values can have any value
                      parsing_insert_query(query_type,keywords,table_name,attr_list,val_list)
                  else:
                      print("Error : Unequal count of attributes and value ")
                      return 0
                  
                  
             else:
                 print("Error :-- VALUES/values Missing")
                 return 0
         else:#incorrect
             print("Error :-- Invalid Table Name")
             return 0
             
         
 else:
     return 0


#checking update statement
def check_update(list):
    query_type="UPDATE QUERY"
    print("__________INSIDE UPDATE FUNCTION_____________")
    a=list[0]
    table_name=list[1]
    b=list[2]
    keywords=[a,b]
    attr_name_list=[]
    val_list=[]
    conditional_variable_list=[]
    operator=""
    
    if (a=="update" and b=="set") or (a=="UPDATE" and b=="SET"):
        if variable_validity_check(table_name)==1:
            
            if "WHERE" in list or "where" in list : #with where condition
              if "WHERE" in list :
                  keywords.append("WHERE")
                  index=list.index("WHERE")
              elif "where" in list:
                  index=list.index("where")
                  keywords.append("where")

              #temp_list equal to without where condition
              temp_list=list[3:index] #only col name and value
              #print("Temp list : ",temp_list)
              s=" "
              s=s.join(temp_list)
              #print("s=",s)
              assign_list=s.split(',')
              #print("Assign list : ",assign_list)
              for k in range(len(assign_list)):
                    #print("Current Assignment : ",assign_list[k])
                    str=assign_list[k]
                    temp_list=str.split('=')
                    if len(temp_list) !=2:
                        print("Error :-- Invalid assignment in : ",str)
                        return 0
                    else:
                        attr_name=temp_list[0]
                        value=temp_list[1]
                        attr_name_list.append(attr_name)
                        val_list.append(value)
                        if (variable_validity_check(attr_name)==1) and value_validity_check(value):
                            continue
                        else:
                            print("Error :-- Invalid Assignment in : ",str)
                            return 0
                            
              
              #to check where condition
              new_condition_list=list[index+1:-1] #after where before ;
              s=""
              s=s.join(new_condition_list)
              element_list=[]
              if "<=" in s:
               element_list=s.split("<=")
               operator="<="
              elif ">=" in s:
               element_list=s.split(">=")
               operator=">="
              elif "<>" in s:
               element_list=s.split("<>")
               operator="<>"
              elif '=' in s:
               element_list=s.split('=')
               operator="="
              elif '<' in s:
               element_list=s.split('<')
               operator="<"
              elif '>' in s:
               element_list=s.split('>')
               operator=">"
              elif '&' in s:
               element_list=s.split('>')
               operator="&"
              elif '|' in s:
               element_list=s.split('>')
               operator="|"

              conditional_variable_list=element_list

              #print("Splitted list : ",element_list)
              if len(element_list) != 2:
               print("Error :--Invalid Condition")
               return 0
              if condition_check(element_list)==1:
               print("Update Statement Pass")
               parsing_update_query(query_type,keywords,table_name,attr_name_list,val_list,conditional_variable_list,operator)
              else:
               print("Error :-- Invalid Condition")
               return 0

            else : #without where condition
                temp_list=list[3:-1] #no need of ;
                s=" "
                s=s.join(temp_list)
                #print("s=",s)
                assign_list=s.split(',')
                #print("Assign list : ",assign_list)
                for k in range(len(assign_list)):
                    #print("Current Assignment : ",assign_list[k])
                    str=assign_list[k]
                    temp_list=str.split('=')
                    if len(temp_list) !=2:
                        print("Error :-- Invalid assignment in : ",str)
                        return 0
                    else:
                        attr_name=temp_list[0]
                        value=temp_list[1]
                        attr_name_list.append(attr_name)
                        val_list.append(value)

                        if (variable_validity_check(attr_name)==1) and value_validity_check(value):
                            continue
                        else:
                            print("Error :-- Invalid Assignment : ",str)
                            return 0
                print("Update Statement Pass")
                parsing_update_query(query_type,keywords,table_name,attr_name_list,val_list,conditional_variable_list,operator)

                   
        else:
            print("Error :-- Invalid Table Name")
    else:
        return 0

#checking delete statement
def check_delete(list):
    query_type="DELETE QUERY"
    print("__________INSIDE DELETE FUNCTION_____________")
    a=list[0]
    b=list[1]
    keywords=[a,b]
    operator=""
    condition_variable_list=[]
    if (a=="delete" and b=="from") or (a=="DELETE" and b=="FROM"):
        #further checking
        if "WHERE" in list or "where" in list: #with where condition
          #print("Inside where condition")
          if "where" in list:
           index=list.index("where")
           keywords.append("where")
          elif "WHERE" in list:
           index=list.index("WHERE")
           keywords.append("WHERE")

          list1=list[:index]
          list1.append(";")
          list2=list[index:]
          #print(list1)
          #for list1 (equal to without where condition)
          table_name=list1[2]
          if variable_validity_check(table_name)==1:
                print("Delete Statement Pass(without condition)")
          else : #incorrect
                print("Error :-- Invalid Table Name")
                return 0
          #print(list2)
          #for list2 checking( where condition)
          s=""
          size=len(list2)
          condition_list=list2[1:size-1]
          #print(condition_list)
          s=s.join(condition_list)
          #print(s)
          element_list=[]
          if "<=" in s:
              element_list=s.split("<=")
              operator="<="
          elif ">=" in s:
              element_list=s.split(">=")
              operator=">="
          elif "<>" in s:
              element_list=s.split("<>")
              operator="<>"
          elif '=' in s:
              element_list=s.split('=')
              operator="="
          elif '<' in s:
              element_list=s.split('<')
              operator="<"
          elif '>' in s:
              element_list=s.split('>')
              operator=">"
          elif '&' in s:
              element_list=s.split('&')
              operator="&"
          elif '|' in s:
              element_list=s.split('|')
              operator="|"

          condition_variable_list=element_list
          #print("Splitted list : ",element_list)
          if len(element_list) != 2:
              print("Error :-- Invalid Condition")
              return 0
          if condition_check(element_list)==1:
              print("Delete Statement Pass")
              parsing_delete_query(query_type,keywords,table_name,condition_variable_list,operator)
          else:
              print("Error :-- Invalid Condition")
              return 0

        else : #without where condition
            table_name=list[2]
            if variable_validity_check(table_name)==1:
                print("Delete Statement Pass")
                parsing_delete_query(query_type,keywords,table_name,condition_variable_list,operator)
            else : #incorrect
                print("Error : Invalid Table Name")
                return 0          
    else :
        return 0


#----------------------------------------------------------------------------------------MAIN CODE----------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("------------------------------PRE-PROCESSING PART------------------------------")    
#opening the input file
file=open("input.txt",'r')
query=file.readlines()
print("Raw Input :- ",query)

#removing extra \n
query=remove_n(query)

#removing extra spces  
if '' in query:
    while '' in query:
        query.remove('')

print("Final Query :- ",query)

#splitting by space
query_word_list=[] #every single word will be an element
for i in range(len(query)):
     temp_string=query[i]
     #print("Temp String : [",i,"]",temp_string)
     temp_list=temp_string.split(' ')
     
     #removing extra space
     temp_list=remove_space(temp_list)
     #print("Temp List : [",i,"]",temp_list)
              
     #adding to the new
     for j in range(len(temp_list)):
          query_word_list.append(temp_list[j])

     
#spcial case (; can be attach with the last word) - to seprate the ;
word=query_word_list[-1]
letter=word[-1]
if letter == ';':
     del query_word_list[-1]
     new_word=word[:-1]
     if new_word !='': #if the word itself is a ;
      query_word_list.append(new_word)
     query_word_list.append(';')
     
print("Final Splitted Query :- ",query_word_list)
print("------------------------------------------------------------------------------------------")    

#---------------------------------------------------------------------------------------------ERROR CHECKING------------------------------------------------------------------------------------
print("------------------------------ERROR CHECKING PART------------------------------")    

#1-semicolon
check=1
count=query_word_list.count(';')
if(count>1):
     print("Error :-- ; Multiple Times Used")
     exit
check=check_semicolon(query_word_list)
if(count==0 or check==0):
     print("Error :-- Missing ; ")
     exit

sql_list=["CREATE","create","DROP",'drop',"SELECT","select","INSERT","insert","UPDATE","update","DELETE","delete"]

#checking the query type
first_word = query_word_list[0]
if first_word in sql_list :
    #2-create
    if check==1: #no previous error
        if first_word=="CREATE" or first_word=="create":
            check=1
            check=check_create(query_word_list)
            if(check==0):
                 print("Error :-- Invalid Create Statement")
         
    #3-drop
    if check ==1:
        if first_word=="DROP" or first_word=="drop":
            check=1
            check=check_drop(query_word_list)
            if(check==0):
                 print("Error :-- Invalid Drop Statement")

    #4-select
    if check==1:
        if first_word=="SELECT" or first_word=="select":
            check=1
            check=check_select(query_word_list)
            if(check==0):
                 print("Error :-- Invalid Select Statement")

    #5-insert
    if check==1:
        if first_word=="INSERT" or first_word=="insert":
            check=1
            check=check_insert(query_word_list)
            if(check==0):
                 print("Error :-- Invalid Insert Statement")

    #6-update
    if check==1:
        if first_word=="UPDATE" or first_word=="update":
            check=1
            check=check_update(query_word_list)
            if(check==0):
                 print("Error :-- Invalid Update Statement")

    #7-delete
    if check==1:
        if first_word=="DELETE" or first_word=="delete":
            check=1
            check=check_delete(query_word_list)
            if(check==0):
                 print("Error :-- Invalid Delete Statement")

else :
    print("Error :-- Invalid SQL Query")

print("------------------------------------------------------------------------------------------")    



