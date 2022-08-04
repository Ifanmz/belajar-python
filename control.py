# var1=""
# while(var1!="exit"):
#     var1=input("Please enter an integer (type exit to exit): ")
#     print(int(var1))

# import sys
# data=''
# while(data!='exit'):
#     try:
#         data=input('Please enter an integer (type exit to exit): ')
#         print('got integer: {}'.format(int(data)))
#     except:
#         if data == 'exit':
#             pass  # exit gracefully without prompt any error
#         else:
#             print('error: {}'.format(sys.exc_info()[0]))