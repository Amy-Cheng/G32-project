import pyaudio
import socket
from threading import Thread
import time
import cv2
import numpy

#音訊格式
FORMAT = pyaudio.paInt16 #取樣格式
CHANNELS = 1 #聲道
RATE = 44100 #取樣率(Hz)
CHUNK = 1024 #緩衝大小(frame)


HOST = ""
PORT1 = 3456
PORT2 = 3457
VIDEO_PORT = 3458
def receiving() :
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((HOST, PORT1))
    serverSocket.listen()
    (clientSocket, address) = serverSocket.accept()
    print( "Connected 1" )

    audio = pyaudio.PyAudio()
    stream = audio.open(format = FORMAT, channels = CHANNELS, rate = RATE,  output = True , frames_per_buffer = CHUNK)
    print("Start")

    try:
        while True:
            data = clientSocket.recv(CHUNK)
            stream.write(data)
    except KeyboardInterrupt:
        pass

    clientSocket.close()
    stream.stop_stream()
    stream.close()
    audio.terminate()

def sending() :
    serverSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket2.bind((HOST, PORT2))
    serverSocket2.listen()

    (clientSocket2, address2) = serverSocket2.accept()
    print("Connected 2")

    audio2 = pyaudio.PyAudio()
    stream2 = audio2.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK)

    try:
        while True:
            sending_data = stream2.read(CHUNK)
            clientSocket2.sendall(sending_data)

    except KeyboardInterrupt:
        pass

    clientSocket2.close()
    stream2.stop_stream()
    stream2.close()
    audio2.terminate()
audio_thread_out = Thread(target = sending)
audio_thread_out.setDaemon( True )
audio_thread_out.start()
time.sleep(0.1)
audio_thread_in = Thread(target = receiving)
audio_thread_in.setDaemon( True )
audio_thread_in.start()

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

time.sleep(0.1)
videoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
videoSocket.bind((HOST, VIDEO_PORT))
videoSocket.listen(True)
conn, addr = videoSocket.accept()

capture = cv2.VideoCapture(0)
ret, frame = capture.read()
encode_param=[ int(cv2.IMWRITE_JPEG_QUALITY), 90 ]

while True:
    length = recvall( conn, 16 )
    if length == None:
        break
    received_stringData = recvall( conn, int(length) )
    received_data = numpy.fromstring( received_stringData, dtype='uint8')
    decimg = cv2.imdecode( received_data, 1 )
    cv2.imshow( 'CLIENT', decimg )
    # 傳資料給client
    if ret != 0 :
        result, imgencode = cv2.imencode( '.jpg', frame, encode_param )
        sending_data = numpy.array( imgencode )
        sending_stringData = sending_data.tostring()
        byte = str(len(sending_stringData)).ljust( 16 )
        conn.send(byte.encode())
        conn.send(sending_stringData)
        ret, frame = capture.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):  #按q键退出
        break

videoSocket.close()
cv2.destroyAllWindows()
capture.release()