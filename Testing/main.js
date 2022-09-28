var board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
  ];
  
  var player1 = 'X';
  var player2 = 'O';
  
  var currentPlayer = player1;
  
  function play(row, col) {
    if (board[row][col] === ' ') {
      board[row][col] = currentPlayer;
  
      if (currentPlayer === player1) {
        currentPlayer = player2;
      } else {
        currentPlayer = player1;
      }
  
      renderBoard();
  
      checkForWinner();
    } else {
      alert('That space is already taken!');
    }
  }
  
  function renderBoard() {
    for (var i = 0; i < board.length; i++) {
      console.log(board[i].join(' | '));
    }
  
    console.log('\n\n');
  }
  
  function checkForWinner() {
    // check rows
  
    for (var i = 0; i < board.length; i++) {
      if (board[i][0] === board[i][1] && board[i][1] === board[i][2]) {
        alert(currentPlayer + ' wins!');
  
        resetBoard();
  
        return; // stop execution of this function! we found a winner!
      }
    }
  
    // check cols
  
    for (var j = 0; j < board.length; j++) {
      if (board[0][j] === board[1][j] && board[1][j] === board[2][j]) {
        alert(currentPlayer + ' wins!');
  
        resetBoard();
  
        return; // stop execution of this function! we found a winner!
      }
    }
  
    // check diags
  
    if (board[0][0] === board[1][1] && board[1][1] === board[2][2]) {
      alert(currentPlayer + ' wins!');
  
      resetBoard();
  
      return; // stop execution of this function! we found a winner!
    } else if (board[0][2] === board[1][1] && board[1][1] === board[2][0]) {
      alert(currentPlayer + ' wins!');
  
      resetBoard();
  
      return; // stop execution of this function! we found a winner!    
    } else if (isBoardFull()) { // check for tie game! all spaces filled and no winner yet...
      alert('Tie game!');
  
      resetBoard();
  
      return; // stop execution of this function! we have a tie game!    
    } else { // no winner yet... keep playing!    
      return; // stop execution of this function! keep playing!    
    }  
  }
  
  function isBoardFull() {
    for (var i = 0; i < board.length; i++) {
      for (var j = 0; j < board[i].length; j++) {
        if (board[i][j] === ' ') {
          return false; // we found an empty space! keep playing!
        }
      }
    }
  
    return true; // all spaces are full! it's a tie game!
  }
  
  function resetBoard() {
    board = [
      [' ', ' ', ' '],
      [' ', ' ', ' '],
      [' ', ' ', ' ']
    ];
  
    currentPlayer = player1;
  
    renderBoard();
  }