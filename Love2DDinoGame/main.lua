function love.load()
    world = love.physics.newWorld(0, 300, true)
    world:setCallbacks(beginContact)

    love.graphics.setBackgroundColor(1, 1, 1)

    dino = {}
    dino.b = love.physics.newBody(world, love.graphics.getWidth()/2, love.graphics.getHeight()/2, "dynamic")
    dino.s = love.physics.newRectangleShape(40, 40)
    dino.f = love.physics.newFixture(dino.b, dino.s)
    dino.f:setUserData("Dino")

    cactus = {}
    cactus.b = {love.physics.newBody(world, love.graphics.getWidth(), love.graphics.getHeight(), "static")}
    cactus.s = {love.physics.newRectangleShape(30, 150)}
    cactus.f = {love.physics.newFixture(cactus.b[1], cactus.s[1])}
    cactus.v = 2

    ground = {}
    ground.b = love.physics.newBody(world, love.graphics.getWidth()/2, love.graphics.getHeight(), "static")
    ground.s = love.physics.newRectangleShape(love.graphics.getWidth(), 20)
    ground.f = love.physics.newFixture(ground.b, ground.s)
    ground.f:setUserData("Ground")

    hitground = false
end

function love.update(dt)
    world:update(dt)

    -- cactus movement
    for i = 1, tablelength(cactus.b) do
        cactus.b[i]:setX(cactus.b[i]:getX() - cactus.v)
    end

    -- append cactus
    if cactus.b[1]:getX() < love.graphics.getWidth()/2  then
        table.insert(cactus.b, 1, love.physics.newBody(world, love.graphics.getWidth(), love.graphics.getHeight(), "static"))
        table.insert(cactus.s, 1, love.physics.newRectangleShape(30, 150))
        table.insert(cactus.f, 1, love.physics.newFixture(cactus.b[1], cactus.s[1]))
    end
end

function love.draw()
    -- cactus
    love.graphics.setColor(0,0,0)
    for i = 1, tablelength(cactus.b) do
        love.graphics.polygon("fill", cactus.b[i]:getWorldPoints(cactus.s[i]:getPoints()))
    end

    -- dino
    love.graphics.polygon("fill", dino.b:getWorldPoints(dino.s:getPoints()))

    -- ground
    love.graphics.polygon("fill", ground.b:getWorldPoints(ground.s:getPoints()))

    -- text
    local dinopos = string.format('dino.x: %d \ndino.y: %d', dino.b:getX(), dino.b:getY())
    local cactuspos = string.format('cactus.x: %d \ncactus.y: %d', cactus.b[1]:getX(), cactus.b[1]:getY())
    love.graphics.print(string.format('%s \nhitground: %s \n%s', dinopos, tostring(hitground), cactuspos), 10, 10)
end

function love.keypressed(key)
    -- dino jump
    if key == 'space' and hitground then
        dino.b:applyForce(0, -25000)
        hitground = false
    end
end

function beginContact(a, b, coll)
    -- only allow to jump if dino hit the ground
    if a:getUserData() == 'Dino' and b:getUserData() == 'Ground' then
        hitground = true
    end

    -- hit the cactus
    if a:getUserData() == 'Dino' and b:getUserData() ~= 'Ground' then
        love.timer.sleep(1)
        love.event.quit('restart')
    end
end

function tablelength(T)
    local count = 0
    for _ in pairs(T) do count = count + 1 end
    return count
end
