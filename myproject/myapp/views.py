from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .enc import distance, speed

from django.http import StreamingHttpResponse
import picamera
import time
import io

def stream_camera(request):
    def stream_generator():
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)  # adjust resolution if needed
            camera.framerate = 24  # adjust framerate if needed
            time.sleep(2)  # camera warm-up time

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                stream.seek(0)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')
                stream.seek(0)
                stream.truncate()

    return StreamingHttpResponse(stream_generator(), content_type='multipart/x-mixed-replace; boundary=frame')

def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')
    

objects = ['apple', 'banana', 'orange']

def welcome(request):
    error_message = None

    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        if search_query in objects:
            return redirect('main')  # Redirect to the next page
        else:
            error_message = 'Object not found. Please try again.'

    return render(request, 'welcome.html', {'error_message': error_message})

def main(request):
	sp = speed()
	dis = distance()
	context = {'speed': sp, 'distance': dis}
	return render(request, 'main.html', context)
    
	
def final(request):
    # Retrieve data for summary (replace these with actual data)
    distance_travelled = 100
    average_speed = 50
    time_taken = 2
    object_received = "Yes"

    context = {
        'distance_travelled': distance_travelled,
        'average_speed': average_speed,
        'time_taken': time_taken,
        'object_received': object_received
    }
    return render(request, 'summary.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')
