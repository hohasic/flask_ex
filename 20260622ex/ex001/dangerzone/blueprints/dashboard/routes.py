from flask import (
    Blueprint, 
    Response, 
    render_template, 
    session, 
    redirect)

from ai.camera_manager import get_frame

import cv2
import time

dashboard_bp = Blueprint(
    'dashboard',
    __name__,
    url_prefix='/dashboard'
)

@dashboard_bp.route('/')
def dashboard():
    
    if session.get('signinedMemberId') is None:
        return redirect('/member/signin_form')
    
    return render_template('dashboard/dashboard.html')

@dashboard_bp.route('/video_feed')
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

def generate_frames():

    while True:

        frame = get_frame()

        if frame is None:
            time.sleep(0.1)
            continue

        ret, buffer = cv2.imencode('.jpg', frame)

        if not ret:
            time.sleep(0.1)
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame_bytes +
            b'\r\n'
        )

        time.sleep(0.03)