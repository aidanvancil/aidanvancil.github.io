// Define your portfolio item data in JSON format
var portfolioItems = [
    {
        keywords: ["math", "dice", "random", "rng", "fun", "game", "domino", "shut", "the", "box", "roll"],
        modalTarget: "#portfolioModal1",
        imageSrc: "assets/img/portfolio/shut_the_box.gif"
    },
    {
        keywords: ["board", "multiplayer", "two-player", "LAN", "local"],
        modalTarget: "#portfolioModal2",
        imageSrc: "assets/img/portfolio/checkers.gif"
    },
    {
      keywords: ["sorting", "algorithm", "data", "visualization", "science"],
      modalTarget: "#portfolioModal3",
      imageSrc: "assets/img/portfolio/sorting.gif"
    },
    {
      keywords: ["social", "media", "talk", "friends", "post", "instagram", "app"],
      modalTarget: '#portfolioModal4',
      imageSrc: "assets/img/portfolio/channel.jpg"
    },
    {
      keywords: ["candy", "data", "science", "math", "colab", "plotting"],
      modalTarget: '#portfolioModal5',
      imageSrc: "assets/img/portfolio/candy.png"
    },
    {
      keywords: ["data", "science", "math", "colab", "plotting", "AI", "ML", "AI/ML"],
      modalTarget: '#portfolioModal6',
      imageSrc: "assets/img/portfolio/hyper.png"
    },
    {
      keywords: ["data", "science", "math", "colab", "plotting", "algorithm", "data", "visualization", "science", "tinder", "recommendation", "dating", "AI", "ML", "AI/ML"],
      modalTarget: '#portfolioModal7',
      imageSrc: "assets/img/portfolio/model.png"
    }
  ];
  
  // Function to generate the portfolio items dynamically
  function generatePortfolioItems() {
    var portfolioContainer = document.getElementById("portfolioContainer");
  
    // Loop through the portfolioItems array and generate HTML for each item
    for (var i = 0; i < portfolioItems.length; i++) {
      var item = portfolioItems[i];
  
      // Create the portfolio item HTML
      var portfolioItem = document.createElement("div");
      portfolioItem.className = "col-md-6 col-lg-4 mb-5 modals";
      portfolioItem.innerHTML = item.keywords.join(" ");
  
      // Create the inner elements for the portfolio item
      var portfolioItemInner = document.createElement("div");
      portfolioItemInner.className = "portfolio-item mx-auto";
      portfolioItemInner.setAttribute("data-bs-toggle", "modal");
      portfolioItemInner.setAttribute("data-bs-target", item.modalTarget);
  
      var portfolioItemCaption = document.createElement("div");
      portfolioItemCaption.className = "portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100";
  
      var portfolioItemCaptionContent = document.createElement("div");
      portfolioItemCaptionContent.className = "portfolio-item-caption-content text-center text-white";
      portfolioItemCaptionContent.innerHTML = '<i class="fas fa-plus fa-3x"></i>';
  
      var portfolioItemImage = document.createElement("img");
      portfolioItemImage.className = "img-fluid";
      portfolioItemImage.src = item.imageSrc;
      portfolioItemImage.alt = "...";
  
      // Append the inner elements to the portfolio item
      portfolioItemCaption.appendChild(portfolioItemCaptionContent);
      portfolioItemInner.appendChild(portfolioItemCaption);
      portfolioItemInner.appendChild(portfolioItemImage);
      portfolioItem.appendChild(portfolioItemInner);
  
      // Append the portfolio item to the container
      portfolioContainer.appendChild(portfolioItem);
    }
  }
  
  // Call the function to generate the portfolio items
  generatePortfolioItems();
  