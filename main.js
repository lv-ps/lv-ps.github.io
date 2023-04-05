let intro = document.querySelector('.intro');
let letter = document.querySelector('.welcome-header');
let letterSpan = document.querySelectorAll('.letter');

window.addEventListener('DOMContentLoaded', () => {

  setTimeout(() => {

    letterSpan.forEach((span, idx) => {
      setTimeout(() => {
        span.classList.add('active');
      }, (idx + 1) * 200)
    });
    setTimeout(() => {
      letterSpan.forEach((span, idx) => {
        setTimeout(() => {
          span.classList.remove('active');
          span.classList.add('fade');
        }, (idx + 1) * 50)
      })
    }, 2000)
    setTimeout(2600)

    setTimeout(() => {
      intro.style.top = '-100vh';

    }, 2000)
  })
})

const wrapper = document.querySelector(".wrapper"),
  qrInput = wrapper.querySelector(".form input"),
  generateBtn = wrapper.querySelector(".form button"),
  qrImg = wrapper.querySelector(".qr-code img");
let preValue;

generateBtn.addEventListener("click", () => {
  let qrValue = qrInput.value.trim();
  if (!qrValue || preValue === qrValue) return;
  preValue = qrValue;
  generateBtn.innerText = "Generating QR Code...";
  qrImg.src = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${qrValue}`;
  qrImg.addEventListener("load", () => {
    wrapper.classList.add("active");
    generateBtn.innerText = "Generate QR Code";
  });
});

qrInput.addEventListener("keyup", () => {
  if (!qrInput.value.trim()) {
    wrapper.classList.remove("active");
    preValue = "";
  }
});

const txts = document.querySelector(".animate-text").children,
  txtsLen = txts.length;

let index = 0;
const textInTimer = 2200,
  textOutTimer = 2000;

function animateText() {
  for (let i = 0; i < txtsLen; i++) {
    txts[i].classList.remove("text-in", "text-out");
  }
  txts[index].classList.add("text-in");

  setTimeout(function() {
    txts[index].classList.add("text-out");
  }, textOutTimer);

  setTimeout(function() {
    if (index == txtsLen - 1) {
      index = 0;
    } else {
      index++;
    }
    animateText();
  }, textInTimer);
}

window.onload = animateText;

window.addEventListener("scroll", () => {
  let scroll = scrollY;
  const overlay = document.querySelector(".overlay");
	
  overlay.style.background = `rgba(0, 0, 0, ${scroll * 1.3 / window.innerHeight})`
})
