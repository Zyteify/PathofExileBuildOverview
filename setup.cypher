//load accounts
LOAD CSV WITH HEADERS FROM 'file:///account.csv' AS row
CREATE (n:Accounts {
    //account id
    account_ID: row.account_ID
    //account name
    , AccountName: row.accounts
    //character name
    , CharacterName: row.names
    //character level
    , CharacterLevel: row.levels
    //character chacter class relationship
    , CharacterClassID: row.classes});


//create index for the account_ID
CREATE INDEX FOR (a:Accounts) ON (a.account_ID);

//load classes
LOAD CSV WITH HEADERS FROM 'file:///classNames.csv' AS row
CREATE (n:Classes {
    //class id
    ClassNames_ID: row.classNames_ID
    //Class name
    , classNames: row.classNames});

//create the relationship between accounts and classes
MATCH (a:Accounts), (c:Classes)
WHERE a.CharacterClassID = c.ClassNames_ID
CREATE (a)-[:IS_CLASS]->(c);

//load uniqueNames
LOAD CSV WITH HEADERS FROM 'file:///uniqueNames.csv' AS row
CREATE (n:UniqueNames {Unique_ID: row.Unique_ID, UniqueName: row.UniqueName, UniqueType: row.UniqueType});

//create index for the Unique_ID
CREATE INDEX FOR (a:UniqueNames) ON (a.Unique_ID);

//create relationship between uniques and the character
LOAD CSV WITH HEADERS FROM 'file:///uniques.csv' AS row
MATCH (u:UniqueNames {Unique_ID: row.Unique_ID}), (a:Accounts {account_ID: row.account_ID})
CREATE (u)-[:USES_UNIQUE]->(a);

//todo check why the cypher commands to create a relationship between the active skill names and accounts doesnt work
//load activeSKillNames
//LOAD CSV WITH HEADERS FROM 'file:///activeSKillNames.csv' AS row
//CREATE (n:ActiveSkillNames {activeSkill_ID: row.activeSkill_ID, activeSkillName: row.activeSkillName, icon: row.icon, activeSkillDPSName: row.activeSkillDPSName});

//create index for the account_ID
//CREATE INDEX FOR (a:ActiveSkillNames) ON (a.activeSkill_ID);

//create relationship between skills and the character
//LOAD CSV WITH HEADERS FROM 'file:///allSkills.csv' AS row
//MATCH (u:ActiveSkillNames {activeSkill_ID: row.activeSkills_ID}), (a:Accounts {account_ID: row.account_ID})
//CREATE (u)-[:USES_ACTIVE_SKILL]->(a);

//load allSKillNames
LOAD CSV WITH HEADERS FROM 'file:///allSKillNames.csv' AS row
CREATE (n:allSkillNames {allSkill_ID: row.allSkill_ID, allSkillName: row.allSkillName, icon: row.icon, allSkillDPSName: row.allSkillDPSName});

//create index for the account_ID
CREATE INDEX FOR (a:allSkillNames) ON (a.allSkill_ID);

//create relationship between skills and the character
LOAD CSV WITH HEADERS FROM 'file:///allSkills.csv' AS row
MATCH (u:allSkillNames {allSkill_ID: row.allSkills_ID}), (a:Accounts {account_ID: row.account_ID})
CREATE (u)-[:USES_ALL_SKILL]->(a);
