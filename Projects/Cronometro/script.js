let timer;
let isRunning = false;
let seconds = 0;
let minutes = 0;

function startStop() {
  if (isRunning) {
    clearInterval(timer);
    document.getElementById("startStop").innerText = "Iniciar";
  } else {
    timer = setInterval(updateTime, 1000);
    document.getElementById("startStop").innerText = "Pausar";
  }
  isRunning = !isRunning;
}

function updateTime() {
  seconds++;
  if (seconds === 60) {
    seconds = 0;
    minutes++;
  }
  document.getElementById("timer").innerText = formatTime(minutes, seconds);
}

function formatTime(mins, secs) {
  return `${mins < 10 ? "0" + mins : mins}:${secs < 10 ? "0" + secs : secs}`;
}

function reset() {
  clearInterval(timer);
  isRunning = false;
  minutes = 0;
  seconds = 0;
  document.getElementById("timer").innerText = "00:00";
  document.getElementById("startStop").innerText = "Iniciar";
}
