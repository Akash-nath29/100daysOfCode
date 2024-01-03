const url = "http://129.213.151.29:6012/"; // Use the correct port

const btn = document.querySelector("button");
const queryInput = document.querySelector("#query");
const linkList = document.querySelector("ul");

btn.addEventListener("click", () => {
    const query = queryInput.value;
    // console.log(query);
    getResult(query);
});

const displayResults = (links) => {
    linkList.innerHTML = ""; // Clear existing results

    links.forEach(link => {
        const truncatedLink = truncateString(link, 50);
        const li = document.createElement("li");
        li.innerHTML = `<a href=${link} target='_blank'>${truncatedLink}</a>`;
        linkList.appendChild(li);
    });
};

const truncateString = (str, maxLength) => {
    return str.length > maxLength ? str.substring(0, maxLength - 3) + "......" : str;
};

const getResult = async (x) => {
    document.querySelector("h1").textContent = "Searching...";
    try {
        const response = await fetch(url + `/${x}`);
        
        if (!response.ok) {
            document.querySelector("h1").textContent = `${response.status}`;
            return;
        }

        const contentType = response.headers.get("content-type");

        if (contentType && contentType.includes("application/json")) {
            const data = await response.json();
            // console.log(data);
            displayResults(data);
        } else {
            console.error("Response is not in JSON format:", await response.text());
        }

        document.querySelector("h1").textContent = "Results";
    } catch (e) {
        console.log(e);
    }
};


