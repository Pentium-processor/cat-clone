#include <stdio.h>
#include <unistd.h>


int main(int argc, char* argv[]){


   int res = getopt(argc,argv,"n"); 
   FILE *fptr;
   char str_buffer[1024]; 
   int count = 0; 

   switch (argc)
   { 

     case 1:
      
      printf("No command line arguments passed\n");
      break;

     case 2: 

      fptr = fopen(argv[1],"r");
      
      break;

     case 3: 

      fptr = fopen(argv[2],"r");

      break;



   }

   if (fptr == NULL)
   { 

     printf("%s: %s: No such file or directory.\n",argv[0],argv[argc-1]);

   } else if ((fptr !=NULL && argc == 2) || argc == 3)

   { 
         
        while (fgets(str_buffer,sizeof(str_buffer),fptr) != NULL)
        { 
          
	   if (argc == 3 && res == 110)
	   {   
	       count++;
               printf("%i %s",count,str_buffer);

	   } else 
	   {

               printf("%s",str_buffer);

	   }


        }
	
	fclose(fptr);


   } 


  return 0;
}
