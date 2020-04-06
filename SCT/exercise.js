function submit () {	
	tags = document.querySelectorAll("div input");
	answers = Array();
	tags.forEach(node => {
		if (node.checked) {
			answers.push(node.value);
		}
	})
	fetch('/submit', {
		method: 'POST',
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify({'answers': answers})
	})
		.then(res => res.json())
		.then(ret => {
			resultTag = document.querySelector("div span[id='result']");
			if (ret === true) {
				resultTag.innerText = "정답입니다.";
			}
			else {
				resultTag.innerText = "오답입니다.";
			}
		
		});
};
