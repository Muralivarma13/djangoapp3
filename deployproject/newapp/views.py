from django.http import JsonResponse
from .models import OrderDetails,MovieBooking,BookDetails
import json
from django.views.decorators.csrf import csrf_exempt

def GetOrders(request):
    try:
        if request.method=="GET":
           result=list( OrderDetails.objects.values())
           print(result)
           if len(result)==0:
               msg="no records found"
           else:
               msg="data retrived successfully"   
           return JsonResponse({"status":"success","message":msg,"data":result,"total no of records":len(result)})
        
        return JsonResponse({"status":"failure","message":"only get method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})
    
    



    

def BookingDetails(request):  
     try:
        if request.method=="GET":
           result=list( MovieBooking.objects.values())
           print(result)
           if len(result)==0:
               msg="no records found"
           else:
               msg="data retrived successfully"   
           return JsonResponse({"status":"success","message":msg,"data":result,"total no of records":len(result)})
        
        return JsonResponse({"status":"failure","message":"only get method allowed"})
     except Exception as e:
        return JsonResponse({"message":"something went wrong"})
      

@csrf_exempt
def orderPlacing(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode("utf-8"))

            OrderDetails.objects.create(
                usermail=data["usermail"],   
                orderid=data["orderid"],     
                amount=data["amount"],       
                mode=data["mode"],
                status=data["status"]
            )

            return JsonResponse(
                {"status": "success", "message": "Order saved successfully"},
                status=201
            )

        return JsonResponse(
            {"error": "Only POST method allowed"},
            status=400
        )

    except KeyError as e:
        return JsonResponse(
            {"error": f"Missing field: {str(e)}"},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=500
        )
@csrf_exempt

def BookMyshow(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            MovieBooking.objects.create(moviename=data["moviename"],
            showtime=data["showtime"],
             screenname=data["screenname"])
            return JsonResponse({"status":"success","msg":"records inserted successfully"})
        else:  
            JsonResponse({"status":"error","message":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})    
    





@csrf_exempt
def insertbook(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)

            BookDetails.objects.create(
                bookname=data.get("bookname"),
                price=data.get("price"),
                author=data.get("author"),
                booktype=data.get("type")   
            )

            return JsonResponse({
                "status": "success",
                "msg": "records inserted successfully"
            })

        else:
            return JsonResponse({
                "status": "error",
                "message": "Only POST method allowed"
            }, status=405)

    except Exception as e:
        print("POST ERROR:", e)
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)


def getdetails(request):
    try:
        if request.method == "GET":
            result1 = list(BookDetails.objects.values())

            return JsonResponse({
                "status": "success",
                "count": len(result1),
                "data": result1
            })

        else:
            return JsonResponse({
                "status": "error",
                "message": "Only GET method allowed"
            }, status=405)

    except Exception as e:
        print("GET ERROR:", e)
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)



@csrf_exempt
def UpdateAuthor(request):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT only"}, status=405)

    data = json.loads(request.body)
    book_id = data.get("id")
    author = data.get("author")

    if not book_id or not author:
        return JsonResponse({"error": "id and author required"}, status=400)

    if not BookDetails.objects.filter(id=book_id).update(author=author):
        return JsonResponse({"error": "not found"}, status=404)

    return JsonResponse({"success": "author updated"})






@csrf_exempt
def DeleteBook(request):
    if request.method == "DELETE":
        book_id = json.loads(request.body).get("id")

        if not book_id:
            return JsonResponse({"error": "id required"}, status=400)

        if not BookDetails.objects.filter(id=book_id).delete()[0]:
            return JsonResponse({"error": "not found"}, status=404)

        return JsonResponse({"success": "deleted"})

    return JsonResponse({"error": "DELETE only"}, status=405)
