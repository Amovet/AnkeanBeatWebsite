//burger menu
const BurgerMenu = document.querySelector('.header__burger-menu');
if(BurgerMenu){
	const menu = document.querySelector(".menu__list");
	BurgerMenu.addEventListener("click", function (e){
		menu.classList.toggle("_active");
	});
}
//search header
const LinkSearch = document.querySelector('.link-search__button');
if(LinkSearch){
	const CloseMenu = document.querySelector(".menu__list");
	const SearchBox = document.querySelector(".link-search");
	const SearchInput = document.querySelector(".link-search__input")
	LinkSearch.addEventListener("click", function (e){
		LinkSearch.classList.toggle("_active");
		CloseMenu.classList.toggle("_close");
		SearchBox.classList.toggle("_open");
		SearchInput.classList.toggle("_open");
	});
}

const button_play = document.getElementById('Button_play')
const canvas = document.getElementById('canvas1')
const ctx = canvas.getContext('2d')
let audioSource
let analyser

button_play.addEventListener('click', function () {
	let audio1 = new Audio('/Audio/button-15.wav')
	const audioContext = new AudioContext()
	audio1.play()
	audioSource = audioContext.createMediaElementSource(audio1)
	analyser = audioContext.createAnalyser()
	audioSource.connect(analyser)
	analyser.connect(audioContext.destination)
	analyser.fftSize = 128
	const bufferLength = analyser.frequencyBinCount
	const dataArray = new Uint8Array(bufferLength)

	const barWidth = canvas.width / bufferLength
	let barHeight
	let x

	function animate() {
		x = 1
		ctx.clearRect(0, 0, canvas.width, canvas.height)
		analyser.getByteFrequencyData(dataArray)
		console.log(dataArray)
		for (let i = 0; i < bufferLength; i++) {
			barHeight = dataArray[i] / 4
			ctx.fillStyle = 'white'
			ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight)
			x += barWidth
		}
		requestAnimationFrame(animate)
	}
	animate()
})
