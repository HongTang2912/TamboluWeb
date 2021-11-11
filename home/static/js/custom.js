
function total() {
    var tot = 0;
    $(".bill").each(function(i){
        var price = $(this).find(".price").html();
        var qu = $(this).find(".count").html();
        $(this).find(".subto").html((parseInt(price) * parseInt(qu)).toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
        tot += parseInt(price) * parseInt(qu);
    });
    var ship = parseInt($(".text-ship").html());
    $(".text-ship").html(ship.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
    $(".text-invoice-price").html(tot.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
    $(".text-total").html((tot+ship).toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));

    const price = [];
    const qu = [];
    var sum = 0;
    $(".table_row").each(function(i){
        price[i] = $(this).find(".column-3").attr("value");
        qu[i] = $(this).find("#p-quantity").attr("value");
        sum += (parseInt(price[i]) * parseInt(qu[i]));
    });
    $(".subtotal").html(sum.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));

    const price_cart = [];
    const qu_cart = [];
    var sumCart = 0;
    $(".header-cart-item-info").each(function(i) {
        price_cart[i] = $(this).find("#price").html();
        qu_cart[i] = $(this).find("#stock").html();
        sumCart += (parseInt(price_cart[i]) * parseInt(qu_cart[i]));
    });
    $(".sub-total").html(sumCart.toLocaleString('it-IT', {style : 'currency', currency : 'VND'})); 
}

$(document).ready(function() {

    

    $("#search").on("keyup", function() {
        var value = $(this).toLowerCase();
        $(".isotope-item div").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexof(value) > -1);
        });
    });
    var content;
   
    var ship; 
    $(document).click(function() {
        $(".select2-selection__rendered").each(function(i) {
            if (i == 1) {
                ship = parseInt($(this).attr("title").slice($(this).attr("title").length - 6, $(this).attr("title").length));
                console.log(ship);
                $(".ship_cost").html(ship.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
                $(".total").html((ship+sum).toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
            }
        });
        
    }); 
    
    $(document).click(function() {
        
        content = "";
        
        $("span[title]").each(function(index) {
            if ($(this).attr("title") != "Choose an option")
                content+=($(this).attr("title") + " ");
        });
        
        document.getElementById("attribute").value = content;
        document.getElementById("num").value = document.getElementById("num-product").value;
        
        
    });

    
    total();
    
    $(".table_row").find("#edit").click(function(){
        $(".result").val($(this).closest("td").attr("value"));
    });
    
    
    //if (edit() == 1) console.log($(this).find("#edit").attr("value"));
 
    //------------------------------------
  
    
    var orderRandom;
    var orderCode = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    for (var i = 0; i < 8; i++) {
        orderCode += possible.charAt(Math.floor(Math.random() * possible.length))
    }
    $('[name="MDH"]').val(orderCode);
    
        
});

