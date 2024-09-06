<script lang="ts">
	import { type ClassValue, clsx } from 'clsx';
	import { twMerge } from 'tailwind-merge';
			
	function cn(...inputs: ClassValue[]) {
		return twMerge(clsx(inputs));
	}
	import Sparkles from '../../lib/Sparkles.svelte';

	let anywhere = "anywhere";

	function getRandomCityName() {
		const cities = ["Dubai", "Paris", "New York", "Shanghai", "Tokyo", "London", "Buenos Aires", "Moscow", "Berlin", "Rome", "Kyiv", "Los Angeles", "Riyadh", "Athens", "Cape Town", "Sydney", "Rio De Janeiro", "San Francisco"];

		const random = Math.floor(Math.random() * cities.length);
		anywhere = `${cities[random]}`;
	}

	function hoverAnywhere() {
		document.getElementById("anywhereSpan").style["backgroundColor"] = ``;
		getRandomCityName();
	}

	let email = "";

	function validateEmail(email) {
		return String(email)
			.toLowerCase()
			.match(
			/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
			);
	};

	let valid = "";

	function submitEmail() {
		if(validateEmail(email)) {
			valid = `You've been added to the newsletter!`;
			email = "";
		} else {
			valid = `${email} is not valid!`;
		}
	}

</script>

<main class="size-full text-white h-screen p-3">
	<nav class="bg-neutral-900 rounded p-3 glow">
		<ul class="p-3 grid grid-cols-2 text-2xl">
			<li class="inline rounded m-1 text-3xl">
				<h1 class="float-left">
					Jimmy's Travel Agency ✈️
				</h1>
			</li>
		</ul> 
	</nav>
	<div class=" h-1/6">

	</div>
	<div class="flex h-[20rem] w-full flex-col items-center justify-center overflow-hidden rounded-md">
			<ul class="grid grid-cols-3 relative z-20 text-center text-3xl font-bold text-white md:text-6xl lg:text-8xl">
				<li class="inline"><div class="moveup glow">Jimmy's</div></li>
				<li class="inline"><div class="moveup glow">Travel</div></li>
				<li class="inline"><div class="moveup glow">Agency</div></li>
			</ul>
		<h1 class="text-center text-2xl text-slate-200 moveup">
			Go to <span on:mouseenter={hoverAnywhere} id="anywhereSpan" class="rounded p-1 italic">{anywhere}</span>.
		</h1>
		<div class="bg-black h-3"></div>
		<div class="relative h-40 w-[40rem]">
			<!-- Gradients -->
			<div
				class="absolute inset-x-20 top-0 h-[2px] w-3/4 bg-gradient-to-r from-transparent via-indigo-500 to-transparent blur-sm"
			/>
			<div
				class="absolute inset-x-20 top-0 h-px w-3/4 bg-gradient-to-r from-transparent via-indigo-500 to-transparent"
			/>
			<div
				class="absolute inset-x-60 top-0 h-[5px] w-1/4 bg-gradient-to-r from-transparent via-sky-500 to-transparent blur-sm"
			/>
			<div
				class="absolute inset-x-60 top-0 h-px w-1/4 bg-gradient-to-r from-transparent via-sky-500 to-transparent"
			/>

			<!-- Core component -->
			<Sparkles
				minSize={0.8}
				maxSize={2}
				particleDensity={300}
				className="w-full h-full"
				particleColor="#FFFFFF"
			/>

			<!-- Radial Gradient to prevent sharp edges -->
			<div class="absolute inset-0 h-full w-full bg-transparent [mask-image:radial-gradient(350px_200px_at_top,transparent_20%,white)]"></div>
		</div>
	</div>
	<div class="grid grid-cols-4 h-2/5">
		<div class="rounded bg-neutral-900 p-3 m-3 moveup glow">
			<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpaperaccess.com%2Ffull%2F489807.jpg&f=1&nofb=1&ipt=45398a78f8eb06ac538603e9b58aec7f3b31d5d8f77b936145405cd3df32f0f4&ipo=images" alt="" class="rounded">
			<br>
			<p class="text-4xl">Dubai</p>
		</div>
		<div class="rounded bg-neutral-900 p-3 m-3 moveup glow">
			<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs1.1zoom.me%2Fb8048%2F487%2FSky_Evening_France_Eiffel_Tower_Paris_From_above_520603_1920x1080.jpg&f=1&nofb=1&ipt=06e453447c28a592e4f0185aedcdf7f05865a33dfc671ab2ad27eec3e0058903&ipo=images" alt="" class="rounded">
			<br>
			<p class="text-4xl">Paris</p>
		</div>
		<div class="rounded bg-neutral-900 p-3 m-3 moveup glow">
			<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.loisirsetevasion.com%2Fwp-content%2Fuploads%2F2015%2F10%2FBuenos-Aires-Argentina.jpg&f=1&nofb=1&ipt=8c9ed882d76cc8b327277232593e1a46f364d3ac7fe944c65d18c0cc35a2adaf&ipo=images" alt="" class="rounded">
			<br>
			<p class="text-4xl">Buenos Aires</p>
		</div>
		<div class="rounded bg-neutral-900 p-3 m-3 moveup glow">
			<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhdqwalls.com%2Fwallpapers%2Ftokyo-tower-0u.jpg&f=1&nofb=1&ipt=e4430088e7659805ed021bdcf089474c22f047beeb8364a4add443c5b2d572b9&ipo=images" alt="" class="rounded">
			<br>
			<p class="text-4xl">Tokyo</p>
		</div>
	</div>
	<div class="h-1/6"></div>
	<div class="grid grid-cols-3">
		<div class="outline outline-1 rounded outline-slate-500 p-2 outline-dotted m-2">
			<h1 class="text-4xl glow">Newsletter</h1>
			<p class="text-slate-500 text-xl">We'll send you updates whenever we add a new destination!</p>
			<div class=" flex justify-content-center">
				<input class="rounded outline outline-1 outline-slate-500 bg-black" type="email" bind:value={email}/>
				<div class="w-1"></div>
				<button class="bg-blue-500 text-center rounded p-1 moveup" on:click={submitEmail}>Submit</button>
			</div>	
			<p class="p-2 text-xl">{valid}</p>
		</div>
		<div class="p-2 m-2 text-slate-500">
			<h1>© 2024 Jimmy's Travel Agency</h1>
		</div>
		<div class="p-2 m-2 text-slate-500">
			<ul>
				<li class="inline">34 A St Enumclaw, WA 98022</li>
				<li class="inline"> | </li>
				<li class="inline">605 475-6968</li>
			</ul>
		</div>
	</div>
</main>
  
<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	main {
		font-family: "Trebuchet MS", Helvetica, sans-serif;
	}
	nav {
		position: fixed;
		left: 0;
		top: 0;
		width: 100%;
		text-align: center;
		z-index: 100;
	}
	body {
		background-image: url("/static/images/c5e86f5b8b8ca4814851465505057de3.jpg");
		background-color: black;
		background-repeat: no-repeat;
	}
	.moveup {
		transition: transform 250ms;
	}
	.moveup:hover {
		transform: translateY(-10px);
	}
	.glow {
		animation: glow 3s ease-in-out infinite alternate;
		text-shadow: 0 0 30px #aaa;
	}
</style>
