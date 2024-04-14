// $(document).ready(function () {
//   console.log("test")
//   var appId = kintone.app.getId();  // Get the current app ID
//   var query = encodeURI('更新日時 > "2012-02-03T09:00:00+0900" and 更新日時 < "2012-02-03T10:00:00+0900" order by レコード番号 asc limit 10 offset 1');
//   var fields = encodeURI('レコード番号,作成日時,ドロップダウン');
  
//   var requestUrl = kintone.api.url('/k/v1/records.json', true) + '?app=' + appId + '&query=' + query + '&fields=' + fields;
//   // Use jQuery to perform the GET request
//   $.ajax({
//       url: requestUrl,
//       type: 'GET',
//     headers: {
//           "Access-Control-Allow-Origin": "https://6o6ugx1o0fs7.cybozu.com",
//           "X-Cybozu-API-Token": "F9wnlx98ze5dbjYgRqRqoGW4JBvxBrNqdsKnPcRJ"
//       },
//       success: function(response) {
//           console.log('Data retrieved successfully:', response);
//           // You can process the response data here and update the DOM as needed
//       },
//       error: function(error) {
//           console.error('Error fetching data:', error);
//       }
//   });
// });

// $(document).ready(function() {

//   // URL of the API endpoint
//   const apiUrl = 'https://6o6ugx1o0fs7.cybozu.com/k/v1/records.json';

//   $.get(apiUrl, function(data) {
//       $('#user-id').text(data.userId);
//       $('#message').text(data.message);
//   }).fail(function() {
//       console.error("Error fetching data");
//   });
// });
