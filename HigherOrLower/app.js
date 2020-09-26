(async function() {
  const inquirer = require('inquirer')
  const axios = require('axios')
  const deckUrl = 'https://deckofcardsapi.com/api/deck'
  console.log('Welcome to Higher or Lower')
  
  let score = 0
  await startGame()

  // Start game
  async function startGame() {
    try {
      // Create deck
      const { data } = await axios.get(`${deckUrl}/new/shuffle/?deck_count=1`)
      // Draw first card
      const { cards } = await drawCard(data.deck_id)
      let currentCard = cards[0]
      // Process turn
      await runTurn(data.deck_id, currentCard)
    } catch(err) {
      console.log('We have experienced an error.')
    }
  }
  
  async function runTurn(deckId, currentCard) {
    // Select higher or lower
    let { value, suit } = currentCard
    console.log(`\nHigher or lower than a ${value} of ${suit}?`)
    // Get answer
    let selection = await promptQuestion()
    // Draw second card
    const { cards } = await drawCard(deckId)
    let newCard = cards[0]
    console.log(`\nNew card: ${newCard.value} of ${newCard.suit}`)
    // Compare cards
    let isCorrect = await compareCards(currentCard.value, newCard.value, selection.answer)
    console.log(`Survey say you are: ${isCorrect ? 'Correct!' : 'Incorrect :('}`)

    if(isCorrect){ 
      score++
      console.log(`\nCurrent Score: ${score}`)
      runTurn(deckId, newCard)
    } else {
      console.log(`\n/*****************/\n/ Final Score: ${score}  /\n/*****************/`)
    }
  }
  
  async function drawCard(deckId) {
    const { data } = await axios.get(`${deckUrl}/${deckId}/draw/?count=1`)
    return data
  }

  function promptQuestion() {
    const questions = [
      {
        type: 'list',
        name: 'answer',
        message: 'Higher or Lower?',
        choices: ['Higher', 'Lower'],
      }
    ]
    return inquirer.prompt(questions).then((answers) => answers);
  }

  async function compareCards(currentCard, newCard, answer) {
    // Process royals
    currentCard = convertRoyals(currentCard)
    newCard = convertRoyals(newCard)
    return answer === 'Higher'
      ? newCard > currentCard ? true : false 
      : newCard < currentCard ? true : false
  }

  function convertRoyals(card) {
    switch(card) {
      case 'ACE': 
        card = 14
        break
      case 'KING': 
        card = 13
        break
      case 'QUEEN': 
        card = 12
        break
      case 'JACK': 
        card = 11
        break
      default: 
        card
        break
    }
    return card
  }
})()