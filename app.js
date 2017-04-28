'use strict';

var Twitter = require('twitter');
var credentials = require('./credentials');

var client = new Twitter({
  consumer_key: credentials.CONSUMER_KEY,
  consumer_secret: credentials.CONSUMER_SECRET,
  access_token_key: credentials.ACCESS_TOKEN_KEY,
  access_token_secret: credentials.ACCESS_TOKEN_SECRET
});

// var params = {screen_name: 'money23green', count: 3};

// client.get('statuses/user_timeline', params, function(error, tweets, response) {
//   if (error) throw error;
//   console.log(tweets[0]['id'])
//   console.log(tweets[0]['user']['id'])
//   console.log(tweets[0]['user']['name'])
//   console.log(tweets[0]['user']['screen_name'])
//   console.log(tweets[0]['created_at']);
//   console.log(tweets[0]['text']);
//   console.log(tweets[0]['entities']);
//   console.log('\n')
//   console.log(tweets[1]['id'])
//   console.log(tweets[1]['user']['id'])
//   console.log(tweets[1]['user']['name'])
//   console.log(tweets[1]['user']['screen_name'])
//   console.log(tweets[1]['created_at']);
//   console.log(tweets[1]['entities']);
//   console.log(tweets[1]['text']);
//   console.log('\n')
//   console.log(tweets[2]['id'])
//   console.log(tweets[2]['user']['id'])
//   console.log(tweets[2]['user']['name'])
//   console.log(tweets[2]['user']['screen_name'])
//   console.log(tweets[2]['created_at']);
//   console.log(tweets[2]['text']);
//   console.log(tweets[2]['entities']);
//   console.log('\n')
//   // tweets.forEach(tweet) {
//   //   console.log(tweet + "\n\n");
//   // }
// });

var params2 = {q:'@money23green', count: 3}
client.get('search/tweets', params2, function(error, tweets, response) {
  if (error) console.log(error);
  console.log(tweets.length);
  console.log(tweets);
});
