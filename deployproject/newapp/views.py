from django.http import JsonResponse
from .models import OrderDetails
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def orderPlacing(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode("utf-8"))

            OrderDetails.objects.create(
                usermail=data["usermail"],   # ✔ matches model
                orderid=data["orderid"],     # ✔ matches model
                amount=data["amount"],       # ✔ DecimalField
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
