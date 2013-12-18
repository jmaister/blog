/* --------------- ENCODE/DECODE --------------- */
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

/* --------------- NUMBERS --------------- */

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

/* --------------- REGULAR EXPRESSIONS --------------- */

var updateRegEx = function() {
    var text = $('#string').val();
    var inputpattern = $('#pattern').val();
    var replace = $('#replace').val();

    // Convert text to RegExp
    var flags = inputpattern.replace(/.*\/([gimy]*)$/, '$1');
    var pattern = inputpattern.replace(new RegExp('^/(.*?)/' + flags + '$'), '$1');
    var regex = new RegExp(pattern, flags);

    // Test
    try {
        var test = regex.test(text);
        $('#pattern-test').val(test);
    } catch (e) {
        $('#pattern-test').val(e);
    }

    try {
        var matches = text.match(regex);
        $('#pattern-match').val(matches.join('\n'));
    } catch (e) {
        $('#pattern-match').val(e);
    }

    try {
        var replaced = text.replace(regex, replace);
        $('#pattern-replaced').val(replaced);
    } catch (e) {
        $('#pattern-replaced').val(e);
    }

};

$('#string').keyup(updateRegEx);
$('#string').keyup();
$('#pattern').keyup(updateRegEx);
$('#pattern').keyup();
$('#replace').keyup(updateRegEx);
$('#replace').keyup();

/* --------------- TIME/DATE --------------- */

var updateTimeDate = function() {
    var millis = $('#millis').val();
    try {
        var date = new Date(+millis);
        $('#date').val(date);
    } catch (e) {
        $('#date').val(e);
    }
    try {
        var date = new Date(+millis).toISOString();
        $('#date-utc').val(date);
    } catch (e) {
        $('#date-utc').val(e);
    }
};
$('#millis').val(+new Date);

$('#millis').keyup(updateTimeDate);
$('#millis').keyup();
