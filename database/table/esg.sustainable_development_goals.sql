USE [ESG]
GO

/****** Object:  Table [esg].[sustainble_development_goals]    Script Date: 3/22/2025 7:31:30 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [esg].[sustainble_development_goals](
	[id] [int] NOT NULL,
	[goal_name] [varchar](200) NOT NULL,
	[goal_desc] [nvarchar](max) NULL,
	[goal_targets] [varchar](200) NULL,
	[target_indicators] [varchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC,
	[goal_name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

