function makeRequestBody(n) {
    return JSON.stringify({ n });
}

function makeRequestHeaders() {
    const requestHeaders = new Headers();
    requestHeaders.append("Content-Type", "application/json");
    return requestHeaders;
}

function makeRequestOptions(n) {
    const headers = makeRequestHeaders();
    const body = makeRequestBody(n);
    return {
        method: 'POST',
        headers,
        body,
        redirect: 'follow',
    };
}

async function getYellowstonePermutationInteger(n) {
    const requestOptions = makeRequestOptions(n);
    const response = await fetch(
        "https://7x9a61i6n3.execute-api.eu-west-2.amazonaws.com/production",
        requestOptions
    );
    return response.text();
}

function getChosenNValue() {
    return document.getElementById('n').value;
}

function preventFormSubmission(event) {
    event.preventDefault();
}

async function displayYellowstonePermutationInteger(event) {
    // NOTE: n is the position of the integer in the Yellowstone sequence. n == 1 corresponds 
    // to the first integer in the sequence.
    try {
        preventFormSubmission(event);
        const n = getChosenNValue();
        const integer = await getYellowstonePermutationInteger(n);
        alert(JSON.parse(integer).body);
    } catch (err) {
        console.log(err);
    }
}

const calculationForm = document.getElementById("calculation-form");
calculationForm.addEventListener("submit", displayYellowstonePermutationInteger);
