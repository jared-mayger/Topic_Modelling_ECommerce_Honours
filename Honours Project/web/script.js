// // Onclick of the button
document.getElementById('button').addEventListener('click', async() =>{
    var query = document.getElementById('hashtaginp').value;
    var amount = document.getElementById('amountinp').value;
    //await eel.send_data("Scraping " + query + " hashtag");
    await eel.scrape(query, amount);
})