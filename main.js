
function getWebSocketServer() {
  if (window.location.host === "localhost:5500") {
    return "ws://localhost:8001/";
  } else {
    return "wss://906e-65-215-196-146.ngrok.io/";
  }
}

const websocket = new WebSocket("ws://10.48.45.131:8001");
console.log(websocket)

websocket.addEventListener('open', (event) => {
  websocket.send('Hello Server!');
});
// window.addEventListener("open", () => {
//     // Open the WebSocket connection and register event handlers.
//     console.log('opeb')
//     //receiveMoves(websocket)
//     websocket.send("coucou")
//   });

// websocket.onopen = function(event) {
//     websocket.send("coucou")
// }

websocket.addEventListener("message", ({ data }) => {
    const event = JSON.parse(data);
    console.log(event)
    websocket.send('data received on the browser')
    // do something with event
  });

// function receiveMoves(websocket) {
//     websocket.addEventListener("message", ({data}) => {
//         //const event = JSON.parse(data);
//         //console.log(event['value']);
//         console.log(data)
//     });
// }

function sendConfirmation(websocket) {
    const event = {status: "received"};
    websocket.send(JSON.stringify(event))
}

