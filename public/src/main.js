   

$(document).ready(function() {
	resulting = [];
	var pullStockData = function(company){
		var Markit = {};
/**
* Define the QuoteService.
* First argument is symbol (string) for the quote. Examples: AAPL, MSFT, JNJ, GOOG.
* Second argument is fCallback, a callback function executed onSuccess of API.
*/



Markit.QuoteService = function(sSymbol, fCallback) {
    this.symbol = sSymbol;
    this.fCallback = fCallback;
    this.DATA_SRC = "http://dev.markitondemand.com/Api/v2/Quote/jsonp";
    this.makeRequest();
};
/**
* Ajax success callback. fCallback is the 2nd argument in the QuoteService constructor.
*/
Markit.QuoteService.prototype.handleSuccess = function(jsonResult) {
    this.fCallback(jsonResult);
};
/**
* Ajax error callback
*/
Markit.QuoteService.prototype.handleError = function(jsonResult) {
    console.error(jsonResult);
};
/** 
* Starts a new ajax request to the Quote API
*/
Markit.QuoteService.prototype.makeRequest = function() {
    //Abort any open requests
    if (this.xhr) { this.xhr.abort(); }
    //Start a new request
    this.xhr = $.ajax({
        data: { symbol: this.symbol },
        url: this.DATA_SRC,
        dataType: "jsonp",
        success: this.handleSuccess,
        error: this.handleError,
        context: this
    });
};
	for(var i = 0; i < company.length; i++){
	new Markit.QuoteService(company[i], function(jsonResult) {

    //Catch errors
    if (!jsonResult || jsonResult.Message){
        console.error("Error: ", jsonResult.Message);
        return;
    }

    //If all goes well, your quote will be here.
    console.log(jsonResult);

    //Now proceed to do something with the data.
    resulting[resulting.length] = jsonResult;
    $("#" + jsonResult.Symbol).text((jsonResult.Name));
    $("#" + jsonResult.Symbol +'currPrice').text('$' + jsonResult.LastPrice);
    $("#" + jsonResult.Symbol +'lowPoint').text('$' + jsonResult.Low);
    $("#" + jsonResult.Symbol +'highPoint').text('$' + jsonResult.High);
    $("#" + jsonResult.Symbol +'change').text('($' + jsonResult.Change.toString().substring(0,4) + ')');
    
    /**	
    * Need help? Visit the API documentation at:
    * http://dev.markitondemand.com
    */

	});

		}

	}

		/*
   	url = 'http://finance.yahoo.com/webservice/v1/symbols/' + company + '/quote?format=json'
   	console.log(url);
   	document.getElementById("mySpanId").innerHTML = url;*/
	
    new WOW().init();
    colors = ['#00e676', '#ffecb3', '#ffb74d'];


    $('#FindStocks').click(function () {
    	 var status = $('#FindStocks').attr('name');
    	 var split = JSON.parse(status);
    	pullStockData(split);
    });
	




});