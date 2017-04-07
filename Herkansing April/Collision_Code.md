	def checkCollisionWithPlayer(self, block):
        
        #Calculate Distance between block and circle
        circleDistanceX = abs(self.xPos - block.xPos);
        circleDistanceY = abs(self.yPos - block.yPos);

        #If circle is too far away on either x or y axis, there is no collision possible
        if (circleDistanceX > (block.w/2 + self.radius)):
            return False
        if (circleDistanceY > (block.h/2 + self.radius)):
            return False

        #Check for Side Collisions
        if (circleDistanceX <= (block.w/2)):
            return True
        if (circleDistanceY <= (block.h/2)):
            return True

        #Check for diagonal Collision
        cornerDistance_sq = (circleDistanceX - block.w/2) ** 2 + (circleDistanceY - block.w/2) ** 2
        
        return (cornerDistance_sq <= (self.radius**2))