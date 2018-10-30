#include<stdio.h>

int main()
{
    int incoming,outgoing,bucket,n,store=0;
    printf("ENTER THE BUCKET SIZE\n");
    scanf("%d",&bucket);
    printf("ENTER THE OUTGOING RATE\n");
    scanf("%d",&outgoing);
    printf("ENTER THE NUMBER OF INPUTS\n");
    scanf("%d",&n);
    while(n!=0)
    {
        printf("ENTER THE INCOMING PACKET SIZE\n");
        scanf("%d",&incoming);
        if(incoming>bucket)
        {
            printf("PACKET %d IS REJECTED AS SIZE IS GREATER THAN BUKCET SIZE\n",incoming);
        }
        else
        {
            while(incoming>0)
            {
                if(incoming<=outgoing)
                {
                    printf("PACKET OF SIZE %d IS TRANSMITTED\n",incoming);
                    break;
                }
                else
                {
                    store=incoming-outgoing;
                    printf("TRANSMITTED %d OUT OF PACKET OF SIZE %d\n",outgoing,incoming);
                    printf("%d REMAINING\n",store);
                    incoming=store;
                }
            }
            
        }
        n--;
    }
}