import './style.css';
import io from 'socket.io-client';

const socket = io('http://127.0.0.1:8000');

socket.on('connect', () => {
  console.log('Connected');
});

socket.on('disconnect', () => {
  console.log('Disconnected');
});

// load Base64 image from server
socket.on('image', (data: { data: string }) => {
  const image = document.querySelector('img')!;
  image.src = `data:image/jpg;base64,${data.data}`;
});

// get datetime from server every second
(function get_datetime() {
  socket.emit('get_datetime', {}, (res: string) => {
    document.querySelector('#now')!.innerHTML = res;
  });

  setTimeout(get_datetime, 1000);
})();
