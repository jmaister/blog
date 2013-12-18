
var transform = function(source, target, func) {
    var srcText = $(source).val();
    try {
        var enc = func(srcText);
        $(target).val(enc);
    } catch (e) {
        $(target).val(e);
    }
};

$('#text').on('keyup', function() {
    transform('#text', '#base64encode', window.btoa);
    transform('#text', '#base64decode', window.atob);
    transform('#text', '#uencode', encodeURI);
    transform('#text', '#udecode', decodeURI);
});
$('#text').keyup();

var changebase = function(source, target, fromBase, toBase) {
    var srcNum = $(source).val();
    try {
        var num = parseInt(srcNum, fromBase);
        var changed = num.toString(toBase);
        $(target).val(changed);
    } catch (e) {
        $(target).val(e);
    }
};

var updateNumbers = function() {
    var fromBase = $('#base').val();
    changebase('#number', '#binary', fromBase, 2);
    changebase('#number', '#decimal', fromBase, 10);
    changebase('#number', '#octal', fromBase, 8);
    changebase('#number', '#hexadecimal', fromBase, 16);
};

$('#number').on('keyup', updateNumbers);
$('#number').keyup();
$('#base').on('change', updateNumbers);
$('#base').change();

