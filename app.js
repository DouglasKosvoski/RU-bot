const fs = require('fs');

var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');

// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(new logger.transports.Console, {
  colorize: true
});

logger.level = 'debug';
// Initialize Discord Bot
var bot = new Discord.Client({
  token: auth.token,
  autorun: true
});

bot.on('ready', function (evt) {
  logger.info('Connected');
  logger.info('Logged in as: ');
  logger.info(bot.username + ' - (' + bot.id + ')');
});

bot.on('message', function (user, userID, channelID, message, evt) {
  // Our bot needs to know if it will execute a command
  // It will listen for messages that will start with `!`
  if (message.substring(0, 1) == '!') {
    var args = message.substring(1).split(' ');
    var cmd = args[0];

    args = args.splice(1);
    switch(cmd) {
      // !ping
      case 'ping':
        bot.sendMessage({
          to: channelID,
          message: 'Pong!'
        });
        break;

      case 'menu':
        fs.readFile('./output.json', 'utf8', (err, data) => {
          if (err) {
            bot.sendMessage({
              to: channelID,
              message: "Error Reading Data :("
            });
            return;
          }
          else {
            // parse JSON string to JSON object
            const asd = JSON.parse(data);
            const xasd = JSON.stringify(asd);
            bot.sendMessage({
              to: channelID,
              message: xasd
            });
          }
        });
        break;
    }
  }
});
