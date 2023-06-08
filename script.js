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

async function displayYellowstonePermutationInteger(n) {
    // NOTE: n is the position of the integer in the Yellowstone sequence. n == 1 corresponds 
    // to the first integer in the sequence.
    try {
        const integer = await getYellowstonePermutationInteger(n);
        alert(JSON.parse(integer).body);
    } catch (err) {
        console.log(err);
    }
}

const calculateButton = document.getElementById("calculate-button");
calculateButton.addEventListener(
    "click",
    () => displayYellowstonePermutationInteger(document.getElementById('n').value)
);
