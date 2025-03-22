USE [ESG]
GO

/****** Object:  Table [esg].[indicators]    Script Date: 3/22/2025 7:29:39 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [esg].[indicators](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[indicator_name] [varchar](500) NOT NULL,
	[indicator_desc] [varchar](max) NULL,
	[indicator_class] [varchar](500) NOT NULL,
	[SDG_id] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [unique_indicator_name] UNIQUE NONCLUSTERED 
(
	[indicator_name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [esg].[indicators]  WITH CHECK ADD FOREIGN KEY([indicator_class])
REFERENCES [esg].[sustainability_metrics] ([name])
GO

